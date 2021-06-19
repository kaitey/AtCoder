def main():
    x, y = list(map(int, input().split()))
    if x == y:
        print(x)
        exit()
    ken = {0, 1, 2}
    ans = ken - {x, y}
    print(list(ans)[0])


if __name__ == '__main__':
    main()
