def main():
    n, a, b = list(map(int, input().split(" ")))
    sm = 0

    for i in range(1, n + 1):
        array = map(int, str(i))
        if a <= sum(array) <= b:
            sm += i

    print(sm)


if __name__ == '__main__':
    main()
