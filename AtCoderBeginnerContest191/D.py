from math import floor, ceil, sqrt


SHIFT = 10 ** 4


def trans(x):
    return int(round(float(x) * SHIFT))


def main():
    x, y, r = list(map(trans, input().split(" ")))
    num = 0

    decided = False
    ya = y - r - 1
    while ya < y + r + 1:
        if not decided and ya % SHIFT != 0:
            ya += 1
            continue
        decided = True
        try:
            xa = sqrt(r ** 2 - (ya - y) ** 2)
        except ValueError:
            ya += SHIFT
            continue
        dia = [x - xa, x + xa]
        num += (floor(dia[1] / SHIFT) - ceil(dia[0] / SHIFT) + 1)
        ya += SHIFT

    print(num)


if __name__ == '__main__':
    main()
