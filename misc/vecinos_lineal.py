matriz = [
    [127, 132, 135, 138],
    [140, 133, 128, 125],
    [139, 139, 136, 127],
    [137, 140, 141, 139]
]

steps = [
    [0,1],
    [1,1],
    [1,0],
    [1, -1],
    [0, -1],
    [-1,-1],
    [-1,0],
    [-1, -1]
]

enabled = ['[0, 0]']
visited = []
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        pivot = matriz[i][j]
        visited.append(str([i,j]))
        if str([i,j]) in enabled:
            print('PIVOTE: ', pivot)
            print('--- VECINOS ---')
            for step_row, step_col in steps:
                new_row = i + step_row
                new_col = j + step_col
                if new_row >= 0 and new_col >= 0 and new_row < len(matriz) and new_col < len(matriz[0]) and str([new_row,new_col]) not in visited:
                    enabled.append(str([new_row,new_col]))
                    vecino = matriz[new_row][new_col]
                    print(vecino)
enabled.sort()
print(enabled)
print(len(enabled))