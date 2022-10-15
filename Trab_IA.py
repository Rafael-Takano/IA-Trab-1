
# SCC0230 - Inteligência Artificial - Trabalho 1

# 
#
# Rafael Kuhn Takano    11200459
# Vitor Amim            11218772


import random
import numpy as np
import search_algorithms
import graphknn  

n, k = 5000,7
v, e = graphknn.generate_knn_graph(n,k)
start_node, end_node = 0, 1

#print(e)
path_bfs, dist_bfs = search_algorithms.BFS(v,e,start_node,end_node)
print(path_bfs, dist_bfs)
#path_bfs, dist_bfs = search_algorithms.BFS(v,e,start_node+1,end_node+1)
#print(path_bfs, dist_bfs)
#path_bfs, dist_bfs = search_algorithms.BFS(v,e,start_node+2,end_node+2)
#print(path_bfs, dist_bfs)
#path_bfs, dist_bfs = search_algorithms.BFS(v,e,start_node+3,end_node+3)
#print(path_bfs, dist_bfs)
#path_bfs, dist_bfs = search_algorithms.BFS(v,e,start_node+4,end_node+4)
#print(path_bfs, dist_bfs)
#path_dfs, dist_dfs = search_algorithms.DFS(v,e,start_node,end_node)
#print(path_dfs, dist_dfs)

path_A_star, dist_A_star = search_algorithms.A_star_algorithm(v,e,start_node,end_node)
print(path_A_star, dist_A_star[end_node])

