MATRIZ = [
    [127, 132, 135, 138],
    [140, 133, 128, 125],
    [139, 139, 136, 127],
    [137, 140, 141, 139]
]

STEPS = [
    [0,1],
    [1,1],
    [1,0],
    [1, -1],
    [0, -1],
    [-1,-1],
    [-1,0],
    [-1, -1]
]

visited = []
def visitar_vecinos(init_row, init_col):
    if str([init_row,init_col]) in visited:
        return
    visited.append(str([init_row, init_col]))
    # print('PIVOTE: ', MATRIZ[init_row][init_col])
    # print('---- VECINOS ----')
    for step_row, step_col in STEPS:
        new_row = init_row + step_row
        new_col = init_row + step_col
        if new_row >= 0 and new_col >= 0 and new_row < len(MATRIZ) and new_col < len(MATRIZ[0]):
            visitar_vecinos(new_row, new_col)
        #     vecino = MATRIZ[new_row][new_col]
        #     # print(vecino)
        

visitar_vecinos(0, 0)