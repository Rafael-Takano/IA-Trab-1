
# SCC0230 - Inteligência Artificial - Trabalho 1

# 
#
# Rafael Kuhn Takano    11200459
# Vitor Amim            11218772

#np.random.shuffle(aux)
import random
import numpy as np
import search_algorithms
import graphknn  

n, k = 50,5
v, e = graphknn.generate_knn_graph(n,k)
path, dist = search_algorithms.BFS(v,e,0,49)
print(path,dist)