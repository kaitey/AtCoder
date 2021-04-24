from math import ceil, floor


def main():
    a, b = list(map(int, input().split()))
    for g in reversed(range(min(10 ** 5, b) + 1)):
        ap = g * ceil(a / g)
        bp = g * floor(b / g)
        if ap != bp and ap <= b and bp >= a:
            print(g)
            return


if __name__ == '__main__':
    main()
