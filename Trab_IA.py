
# SCC0230 - Inteligência Artificial - Trabalho 1

# 
#
# Rafael Kuhn Takano        11200459
# Vinicius S. F. Kuhlmann   11215751
# Vitor Amim                11218772

from graphknn import KnnGraph
from statistics import mean
from timeit import default_timer as timer

testing = [(10, 3), (10, 5)]
deploy =  [(5000, 3), (5000, 5), (5000, 7)]

with open('experimentos.txt', 'w') as f:
    for experiment_num, experiment_values in enumerate(deploy):
        n, k = experiment_values
        f.write(f"=========== EXPERIMENTO {experiment_num+1}: n={n}, k={k} ==========\n\n")
        knn = KnnGraph(10, 2)
        methods = [
            ("Depht-First", knn.iterative_DFS), 
            ("Breadth-First", knn.BFS), 
            ("Best-First", knn.best_first),
            ("A*", knn.a_star)]
        test_cases = knn.random_start_goals(20)
        for method_name, method in methods:
            f.write(f"{method_name}:\n")
            start = timer()
            results = [method(start, goal) for start, goal in test_cases]
            results = [result for result in results if result[0] is not None] # remove None
            end = timer()
            f.write(f"Tempo de execução: {end-start} segundos\n")
            f.write(f"Distância média percorrida: {mean(result[1] for result in results)}\n\n")