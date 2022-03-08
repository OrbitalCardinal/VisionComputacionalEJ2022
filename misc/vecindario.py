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

di = 10
asignaciones = {}
n_rows = len(matriz)
n_cols = len(matriz[0])
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        pivot = matriz[i][j]
        pivot_plus = pivot + di
        pivot_min = pivot - di
        print('Pivote: ',pivot)
        print('---- VECINOS ----')
        for step_row, step_col in steps:
            new_row = i + step_row
            new_col = j + step_col
            if new_row >= 0 and new_col >= 0 and new_row < n_rows and new_col < n_cols :
                neighbor = matriz[new_row][new_col]
                if neighbor >= pivot_min and neighbor <= pivot_plus:
                    print(neighbor, ' PERTENECE')
                else:
                    print(neighbor, ' NO PERTENECE')
    print('--------')