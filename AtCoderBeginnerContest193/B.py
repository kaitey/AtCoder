def main():
    n = int(input())
    money = 10000000000
    for _ in range(n):
        a, p, x = list(map(int, input().split(" ")))
        if x - a > 0:
            money = min(money, p)
    if money == 10000000000:
        print("-1")
    else:
        print(money)


if __name__ == '__main__':
    main()
