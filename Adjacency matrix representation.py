n = 5
graph = [[0 for _ in range(n)] for _ in range(n)]

def add_edge(u, v):
    graph[u][v] = 1
    graph[v][u] = 1

add_edge(0, 1)
add_edge(0, 4)
add_edge(1, 2)
add_edge(1, 3)
add_edge(1, 4)
add_edge(2, 3)
add_edge(3, 4)

print("Adjacency Matrix Representation:")
for row in graph:
    print(row)
