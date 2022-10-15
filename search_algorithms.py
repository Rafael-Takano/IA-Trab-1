import numpy as np
import queue
from queue import PriorityQueue

def invert_list(list):
    list_end = []
    if(len(list) == 0):
        return list_end
    while len(list) > 1: 
        list_end.append(list[-1])
        list = list[0]
    if list:        
        list_end.append(list[0])
    return list_end

def dist_between_vertices(v_list, v1, v2): 
    return np.sqrt(np.power(v_list[v1][0]-v_list[v2][0],2)+np.power(v_list[v1][1]-v_list[v2][1],2))

def recursiveDFS(v_list, e_list, v_start, v_end, visited):     
    if (v_start == v_end):
        return [v_end], dist_between_vertices(v_list, v_start, v_end) 

    visited[v_start] = 1
    for v in e_list[v_start]: 
        if (not visited[v]):
            path, dist = recursiveDFS(v_list, e_list, v, v_end, visited)             
            if (dist != -1): 
                return [path,v_start], dist+dist_between_vertices(v_list, v_start, v) 

    return [], -1
def DFS(v_list, e_list, v_start, v_end): 

    visited = np.zeros(len(v_list))
    #path, total_dist = recursiveDFS(v_list, e_list, v_start, v_end, visited)
    stack = []
    memory = []

    stack.append(v_start)
    while stack:        
        u = stack.pop()
        if (not visited[u]):
            visited[u] = 1
            if(u == v_end): 
                break
            for w in e_list[u]: 
                stack.append(w)
                memory.append([u,w])
    
    if(visited[v_end]):
        path = [v_end]
        total_dist = 0
        for memory in reversed(memory): 
            if(path[-1] == memory[1]): 
                total_dist += dist_between_vertices(v_list, path[-1], memory[0])
                path = [path,memory[0]]

        return invert_list(path), total_dist
    
    return [], -1
             

def BFS(v_list, e_list, v_start, v_end): 
    path = []
    total_dist = 0
    visited = np.zeros(len(v_list))
    Q = queue.Queue()

    memo = []

    Q.put(v_start) 
    visited[v_start] = 1

    while not Q.empty():
        u = Q.get()
        for w in e_list[u]:
            if(not visited[w]): 
                Q.put(w)
                memo.append([u,w])
                visited[w] = 1    
        if(visited[v_end]):
            break
    if(visited[v_end]):
        path = [v_end]
        for memory in reversed(memo): 
            if(path[-1] == memory[1]): 
                total_dist += dist_between_vertices(v_list, path[-1], memory[0])
                path = [path,memory[0]]

        return invert_list(path), total_dist
    return [], -1

def Best_First(v_list, e_list, v_start, v_end): 
    path = []
    total_dist = 0

    visited = np.zeros(len(v_list))    

    p_queue = [[dist_between_vertices(v_list,v_start,v_end),v_start]]

    memo = []
    
    visited[v_start] = 1

    while p_queue:
        u = p_queue.pop()
        for w in e_list[u[1]]:
            if(not visited[w]): 
                p_queue.append([dist_between_vertices(v_list,w,v_end),w])
                memo.append([u[1],w])
                visited[w] = 1    
        
        p_queue.sort(reverse=True)
        if(visited[v_end]):
            break
    if(visited[v_end]):
        path = [v_end]
        for memory in reversed(memo): 
            if(path[-1] == memory[1]): 
                total_dist += dist_between_vertices(v_list, path[-1], memory[0])
                path = [path,memory[0]]

        return invert_list(path), total_dist
    return [], -1    

def A_algorithm(v_list, e_list, v_start, v_end): 
    path = []
    total_dist = 0
    return path, total_dist
    
def A_star_algorithm(v_list, e_list, v_start, v_end): 
    queue = PriorityQueue()
    queue.put(v_start, 0)
    came_from = np.array([None]*len(v_list))
    cost_so_far = np.array([None]*len(v_list))
    came_from[v_start] = None
    cost_so_far[v_start] = 0
    visited = np.zeros(len(v_list))
    
    while not queue.empty():
        current = queue.get()
        
        if current == v_end:
            break
        
        for next in e_list[current]:
            new_cost = cost_so_far[current] + dist_between_vertices(v_list, current, next)
            if visited[next] == 0 or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + dist_between_vertices(v_list, next, v_end)
                queue.put(next, priority)
                came_from[next] = current
                visited[next] = 1
    
    inverted_path = []
    tmp = came_from[v_end]
    count = 0
    for i in range(len(came_from)):
        inverted_path.append(tmp)
        count += 1
        if(tmp == v_start):
            break 
        tmp = came_from[tmp]   
    
    path = []
    for i in range(count):
        path.append(inverted_path.pop())
    path.append(v_end)
    return path, cost_so_far