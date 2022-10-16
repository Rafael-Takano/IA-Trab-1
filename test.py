from graphknn import KnnGraph

knn = KnnGraph(10, 2)
start, end = list(knn.random_start_goals(1))[0]
result = knn.iterative_DFS(start, end)
print(result)