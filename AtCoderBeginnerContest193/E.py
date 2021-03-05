def calc():
    x, y, p, q = list(map(int, input().split(" ")))
    if (2 * x + 2 * y) % (p + q) == 0:
        print("infinity")
        return
    if y >= q:
        i = 0
        while True:
            for c in range(x + (2 * x + 2 * y) * i, x + y + (2 * x + 2 * y) * i):
                if c % (p + q) == p:
                    print(c)
                    return
            i += 1
    else:
        i = 0
        while True:
            for c in range(p + (p + q) * i, (p + q) * (i + 1)):
                if c % (2 * (x + y)) == x:
                    print(c)
                    return
            i += 1


def main():
    t = int(input())
    for _ in range(t):
        calc()


if __name__ == '__main__':
    main()
