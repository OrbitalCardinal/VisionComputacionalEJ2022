import numpy as np

# matrix = np.random.rand(4,4) * 10
matrix = np.array([
    [100, 90, 110, 90],
    [200, 210, 190, 100],
    [300, 300, 200, 90],
    [400, 300, 110, 110]
])

moves = [
    [-1,0],
    [-1,1],
    [0,1],
    [1,1],
    [1,0],
    [1,-1],
    [0,-1],
    [-1,-1]
]

graph = {}
state = {}

# Define states
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        neighbors = []
        for move in moves:
            neighbor_i = i + move[0]
            neighbor_j = j + move[1]
            if neighbor_i >= 0 and neighbor_j >= 0 and neighbor_i < matrix.shape[0] and neighbor_j < matrix.shape[1]:
                neighbors.append(f'{i + move[0]},{j + move[1]}')
                graph[f'{i},{j}'] = neighbors
                state[f'{i},{j}'] = 0

visited = set() # Set to keep track of visited nodes.
state_counter = 1
di = 10
def dfs(visited, graph, node, matrix, pivot):
    if node not in visited:
        print (node)
        visited.add(node)
        i, j = node.split(',')
        state[f'{int(i)},{int(j)}'] = state_counter
        for neighbour in graph[node]:
            i_n, j_n = neighbour.split(',')
            value_n = matrix[int(i_n), int(j_n)]
            if value_n >= pivot - di and value_n <= pivot + di:
                state[f'{i},{j}'] = state_counter
                dfs(visited, graph, neighbour, matrix, pivot)

# Driver Code
for key in graph.keys():
    i,j = key.split(',')
    dfs(visited, graph, f'{i},{j}', matrix, matrix[int(i),int(j)])
    state_counter += 1
print(state)