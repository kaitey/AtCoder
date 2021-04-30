def main():
    r, x, y = list(map(int, input().split()))
    dis = x ** 2 + y ** 2
    if dis < r ** 2:
        print("2")
        return
    if dis == r ** 2:
        print("1")
        return
    n = 2
    while True:
        if dis <= (n * r) ** 2:
            print(n)
            return
        n += 1


if __name__ == '__main__':
    main()
