from math import floor, ceil, sqrt
from copy import deepcopy


def main():
    x, y, r = list(map(float, input().split(" ")))
    x_diameter = [ceil(x-r), floor(x+r)]
    num = 0
    tmp_dia = deepcopy(x_diameter)
    for ya in range(ceil(y), floor(y+r) + 1):
        dia = [0, -1]
        for xa in range(tmp_dia[0], tmp_dia[1]+1):
            if sqrt((xa - x) ** 2 + (ya - y) ** 2) <= r:
                dia[0] = xa
                break
        for xa in range(tmp_dia[1], tmp_dia[0]-1, -1):
            if sqrt((xa - x) ** 2 + (ya - y) ** 2) <= r:
                dia[1] = xa
                break
        num += (dia[1] - dia[0] + 1)
        tmp_dia = deepcopy(dia)

    if floor(y) == ceil(y):
        start_y = floor(y) - 1
    else:
        start_y = floor(y)

    tmp_dia = deepcopy(x_diameter)
    for ya in range(start_y, ceil(y-r) - 1, -1):
        dia = [0, -1]
        for xa in range(tmp_dia[0], tmp_dia[1]+1):
            if sqrt((xa - x) ** 2 + (ya - y) ** 2) <= r:
                dia[0] = xa
                break
        for xa in range(tmp_dia[1], tmp_dia[0]-1, -1):
            if sqrt((xa - x) ** 2 + (ya - y) ** 2) <= r:
                dia[1] = xa
                break
        num += (dia[1] - dia[0] + 1)
        tmp_dia = deepcopy(dia)
    print(num)


if __name__ == '__main__':
    main()
