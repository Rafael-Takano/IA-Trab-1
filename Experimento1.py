import numpy as np
import graphknn

deploy = (50, 5)

with open('experimento1.txt','w',encoding='utf-8') as f:
    n,k = deploy
    f.write(f"=========== EXPERIMENTO 1: n={n}, k={k} ==========\n\n")
    knn = graphknn.KnnGraph(n,k)
    methods = [
            ("Depht-First", knn.iterative_DFS),
            ("Breadth-First", knn.BFS),
            ("Best-First", knn.best_first),
            ("A Half", knn.a_pessimist),
            ("A*", knn.a_star)]
    knn.plot()
    test_case = knn.random_start_goals(1)
    for method_name, method in methods:
            f.write(f"{method_name}:\n")            
            result = method(test_case[0][0], test_case[0][1]) 
            caminho =  result[0]               
            distance = result[1] 
            f.write(f"Caminho percorrido: {caminho}\n" ) 
            f.write(f"Distância percorrida: {distance}\n\n")            