import random
import numpy as np

def generate_vertices(n):
    vertices = []
    for i in range(n):
        x = random.randint(0,n)
        y = random.randint(0,n)
        coordinates = (x,y)
        vertices.append(coordinates)
    return vertices

def generate_edges(n, k):
    
    isFull = np.zeros(n) # Guarda o número de arestas que cada vértice possui
    edgesMatrix = []

    for currentNode in range(n):
        edges = []
        for i in range(k):
            edges.append(-1)

        aux = np.arange(currentNode + 1, n) # Cria um array com todos os vértices possíveis, os nós de iterações anteriores e o atual não entram nas opções
        np.random.shuffle(aux) # Embaralha os vértices aleatoriamente

        #Prioriza vertices com menos arestas
        #tmp = np.arange(0, 1) 
        #for i in range(k):
        #    for j in range(aux.size):
        #        if (isFull[aux[j]] == i):
        #            tmp = np.append(tmp, aux[j])
        #aux = tmp
        #aux = np.delete(aux, 0)

        count = 0
        #Caso um vertice anterior aponte para o vertice atual, adiciona o vertice anterior em suas arestas
        for i in range (currentNode):
            for j in range (k):
                if(edgesMatrix[i][j] == currentNode):
                    edges[count] = i
                    count += 1
                    #aux = np.delete(aux, np.where(aux == i)) # Remove o vértice adicionado das opções

       #Adiciona arestas possiveis até que o vertice atual tenha k arestas              
        while(aux.size > 0 and isFull[currentNode] < k):
            #print(aux)
            if(isFull[aux[0]] < k):
                edges[count] = aux[0]
                count += 1
                isFull[currentNode] += 1
                isFull[aux[0]] += 1
            aux = np.delete(aux, 0) # Remove o vértice das opções

        edgesMatrix.append(edges)
    return edgesMatrix

def generate_knn_graph(n,k):
    vertice_list = generate_vertices(n)
    edge_list = generate_edges(n,k)
    return vertice_list,edge_list