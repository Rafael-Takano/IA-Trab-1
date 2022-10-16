from dis import dis
import random
import numpy as np
from dataclasses import dataclass
from queue import Queue, PriorityQueue

@dataclass(frozen=True, order=True)
class Vertex:
    """ Armazena as coordenadas e possui uma função de distância entre vértices

    Por ser um dataclass, já vem com todo o boilerplate de dunder methods 
    como __init__, __repr__, __eq__, __hash__, etc. """
    x: float
    y: float
    
    def dist(self, other):
        """ Distância euclidiana entre dois vértices """
        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __iter__(self):
        return iter((self.x, self.y))

class KnnGraph:
    """ Representa um grafo não direcionado com pesos nas arestas. 
    
    Vértices são armazenados em uma lista de objetos Vertex.
    Arestas são armazenadas em um dicionário. O grafo tem pesos,
    mas os pesos não precisam ser armazenados, pois podem ser
    calculados a partir dos vértices sempre que necessário. """

    def __init__(self, n, k):
        self.n = n
        self.k = k

        # Vertices
        i = 0
        vertices = set()
        while i < n:
            x = round(random.uniform(1, n-1), 3)
            y = round(random.uniform(1, n-1), 3)
            vertex = Vertex(x, y)
            if vertex in vertices:
                continue
            vertices.add(vertex)
            i += 1

        # Arestas
        edges = {vertex: set() for vertex in vertices}
        for origin in vertices:
            i = 0
            while i + len(edges[origin]) < k:
                neighbour = random.choice(list(vertices - {origin}))
                if neighbour in edges[origin]: # Se a aresta já existe, encontre outra aresta
                    continue
                    
                # Aresta não existe, então adiciona e incrementa o contador
                edges[origin].add(neighbour)
                edges[neighbour].add(origin)
                i += 1

        self.vertices = vertices
        self.edges = edges
    
    def plot(self, distances=False):
        """ Plota os vértices e as arestas do grafo. """
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 10))
        for vertex in self.vertices:
            plt.scatter(*vertex, color='red', s=30)
            plt.text(*vertex, f"{vertex}", fontsize=8)
        for vertex, edge in self.edges.items():
            for neighbour in edge:
                plt.plot(*zip(vertex, neighbour), c='black', alpha=0.2)
                if distances:
                    plt.text((vertex.x + neighbour.x)/2, (vertex.y + neighbour.y)/2,
                        round(vertex.dist(neighbour), 2), ha='center', va='center')
        plt.show()
    
    def random_start_goals(self, amount):
        """ Retorna uma certa quantidade de pares de vértices aleatórios. """
        start_goals = []
        for _ in range(amount):
            start = random.choice(list(self.vertices))
            goal = random.choice(list(self.vertices - {start}))
            start_goals.append((start, goal))
        return start_goals
    
    def __recursive_DFS(self, start, goal, visited=None):
        """ Busca em profundidade recursiva. """
        if start == goal:
            return [goal], start.dist(goal) # Retorna o caminho e a distância
        
        if not visited:
            visited = set()
        visited.add(start)
        for vertex in self.edges[start]: 
            if vertex in visited: # Vértice já foi visitado, ignora
                continue
            path, dist = self.__recursive_DFS(vertex, goal, visited)             
            if dist is not None:                # Vértice foi encontrado
                return (path + [start],         # Adiciona ao caminho
                    dist + start.dist(vertex))  # Adiciona à distância
        
        return None, None # Vértice não foi encontrado
    
    def recursive_DFS(self, start, goal):
        """ Busca em profundidade. """
        path, dist =  self.__recursive_DFS(start, goal)
        return list(reversed(path)), dist

    def iterative_DFS(self, start, goal):
        """ Busca em profundidade iterativa. """

        visited = set()
        stack = [start]
        memory = []

        # Atravessa o grafo até encontrar o vértice final, e salva o caminho
        # percorrido na variável memória.
        # A diferença para a busca em largura é que a busca em profundidade
        # usa uma pilha ao invés de uma fila, acessando os vértices em ordem
        # de profundidade ao invés de distância.
        while stack:
            vertex = stack.pop()
            if vertex in visited:
                continue
            visited.add(vertex)
            if vertex == goal:
                return self.reconstruct_path(goal, memory)
            stack += self.edges[vertex] # Adiciona os vizinhos ao topo da pilha
            memory.append(vertex)
        
        return None, None

    def BFS(self, start, goal):
        """ Busca em largura. """

        visited = {start}
        queue = Queue()
        queue.put(start)
        memory = []

        # Atravessa o grafo até encontrar o vértice final, e salva o caminho
        # percorrido na variável memória.
        # A diferença para a busca em profundidade é que a busca em largura
        # usa uma fila ao invés de uma pilha, acessando os vértices em ordem
        # de distância do vértice inicial ao invés de profundidade.
        while not queue.empty():
            vertex = queue.get()
            memory.append(vertex)
            for neighbor in self.edges[vertex]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                if neighbor == goal: # Vértice final encontrado
                    return self.reconstruct_path(goal, memory)
                queue.put(neighbor)
        
        return None, None

    def best_first(self, start, goal):
        """ Busca de melhor caminho. 
        
        Exatamente igual à busca em largura, mas usa uma fila de prioridade
        ao invés de uma fila normal, para que os vértices com a menor distância
        ao vertice final sejam acessados primeiro. """

        visited = {start}
        queue = PriorityQueue()
        queue.put((start.dist(goal), start))
        memory = []

        while not queue.empty():
            vertex = queue.get()[1]
            memory.append(vertex)
            for neighbor in self.edges[vertex]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                if neighbor == goal: # Vértice final encontrado
                    return self.reconstruct_path(goal, memory)
                priority = neighbor.dist(goal)
                queue.put((priority, neighbor)) # Adiciona a distância ao vértice final como prioridade
        
        return None, None

    def __a(self, start, goal, h):
        """ Busca A """

        queue = PriorityQueue()     # Fila de prioridade que armazena os vértices a serem visitados
        queue.put((h(start), start))
        came_from = {}              # Guarda o vértice anterior de cada vértice no caminho

        # Custo do menor caminho do vértice até o vértice inicial
        g_score = {vertex: float('inf') for vertex in self.vertices - {start}}
        g_score[start] = 0

        # Estimativa do menor caminho até o vértice final se passar pelo vértice
        f_score = {vertex: float('inf') for vertex in self.vertices - {start}}
        f_score[start] = h(start)

        while not queue.empty():
            current = queue.get()[1] # Vértice com o menor f_score
            if current == goal:
                return self.unravel_came_from(came_from, current)
            for neighbor in self.edges[current]:
                g_score_candidate = g_score[current] + current.dist(neighbor)
                if g_score_candidate >= g_score[neighbor]: # O novo caminho não é melhor que o anterior
                    continue
                # O novo caminho é melhor que o anterior, então atualiza os valores
                came_from[neighbor] = current
                g_score[neighbor] = g_score_candidate
                f_score[neighbor] = g_score_candidate + h(neighbor)
                if neighbor not in queue.queue: # queue.queue retorna os elementos da fila
                    queue.put((f_score[neighbor], neighbor))

        # Fila vazia, não há caminho
        return None, None
    
    def a_half(self, start, goal):
        """ Busca A* com heurística de distância euclidiana ao quadrado. """
        return self.__a(start, goal, lambda n: n.dist(goal) / 2)
    
    def a_star(self, start, goal):
        """ Busca A* com heurística de distância euclidiana. """
        return self.__a(start, goal, lambda n: n.dist(goal))

    def unravel_came_from(self, came_from, current):
        """ Reconstrói o caminho a partir do dicionário came_from,
        que é basicamente uma lista encadeada de vértices. """
        path = [current]
        dist = 0
        while current in came_from.keys():
            current = came_from[current]
            dist += current.dist(path[-1])
            path.append(current)
        return list(reversed(path)), dist

    def reconstruct_path(self, goal, memory):
        """ Reconstrói o caminho percorrido a partir de vértices visitados por um algoritmo de busca. 
        
        Para encontrar o caminho, percorre a memória de trás para frente,
        adicionando somente os vértices cuja lista de adjacência conter
        o vértice adicionado mais recentemente ao caminho. """
        path = [goal]
        dist = 0
        for vertex in reversed(memory):
            if path[-1] not in self.edges[vertex]: # O vértice não faz ligação com o caminho
                continue
            dist += vertex.dist(path[-1])
            path.append(vertex)

        return list(reversed(path)), dist