from webbrowser import get
import numpy as np


def dist_between_vertices(v_list, v1, v2): 
    return np.sqrt(np.power(v_list[v1][0]-v_list[v2][0],2)+np.power(v_list[v1][1]-v_list[v2][1],2))

def recursiveDFS(v_list, e_list, v_start, v_end, visited):     
    if (v_start == v_end):
        return [v_end], dist_between_vertices(v_list, v_start, v_end) 

    visited[v_start] = 1
    for v in e_list[v_start]: 
        if (visited[v] == 0):
            path, dist = recursiveDFS(v_list, e_list, v, v_end, visited)             
            if (dist != -1): 
                return [path,v_start], dist+dist_between_vertices(v_list, v_start, v) 

    return [], -1
def DFS(v_list, e_list, v_start, v_end): 

    visited = np.zeros(len(v_list))
    path, total_dist = recursiveDFS(v_list, e_list, v_start, v_end, visited)
             

    return path, total_dist

def BFS(v_list, e_list, v_start, v_end): 
    path = []
    total_dist = 0
    return path, total_dist

def Best_First(v_list, e_list, v_start, v_end): 
    path = []
    total_dist = 0
    return path, total_dist

def A_algorithm(v_list, e_list, v_start, v_end): 
    path = []
    total_dist = 0
    return path, total_dist
    
def A_star_algorithm(v_list, e_list, v_start, v_end): 
    path = []
    total_dist = 0
    return path, total_dist