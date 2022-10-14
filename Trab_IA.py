
# SCC0230 - Inteligência Artificial - Trabalho 1

# 
#
#
# Vitor Amim  11218772

#np.random.shuffle(aux)
import random
import numpy as np

n = 10
k = 2

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

        aux = np.arange(0, n) # Cria um array com todos os vértices possíveis
        aux = np.delete(aux, np.where(aux == currentNode)) # Remove o vértice atual das opções
        np.random.shuffle(aux) # Embaralha os vértices aleatoriamente

        count = 0
        #Caso um vertice anterior aponte para o vertice atual, adiciona o vertice anterior em suas arestas
        for i in range (currentNode):
            for j in range (k):
                if(edgesMatrix[i][j] == currentNode):
                    edges[count] = i
                    count += 1
                    aux = np.delete(aux, np.where(aux == i)) # Remove o vértice adicionado das opções

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
    print(edgesMatrix)

generate_edges(n, k)