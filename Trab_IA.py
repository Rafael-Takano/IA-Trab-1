
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

n, k = 5000,7
v, e = graphknn.generate_knn_graph(n,k)
start_node, end_node = 0, 49
path_bfs, dist_bfs = search_algorithms.BFS(v,e,start_node,end_node)
path_gbs, dist_gbs = search_algorithms.Best_First(v,e,start_node,end_node)
path_dfs, dist_dfs = search_algorithms.DFS(v,e,start_node,end_node)


print(path_bfs, dist_bfs)
print(path_gbs, dist_gbs)
print(path_dfs, dist_dfs)