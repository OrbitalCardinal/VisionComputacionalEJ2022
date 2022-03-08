import sys

def obtener_rangos(s):
    s = int(s)
    m = 255
    step = m // s
    range_list = []
    sum_ = 0
    for i in range(s):
        range_list.append(sum_)
        sum_ = sum_ + step
    range_list.append(m)
    return range_list

print(obtener_rangos(sys.argv[1]))
