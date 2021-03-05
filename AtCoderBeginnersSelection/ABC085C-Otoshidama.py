def main():
    n, y = list(map(int, input().split(" ")))
    for a in range(n + 1):
        for b in range(n - a + 1):
            num = [a, b, n - a - b]
            if y == clac_money(num):
                print(*num)
                return
    print("-1 -1 -1")


def clac_money(num):
    money = 10000 * num[0] + 5000 * num[1] + 1000 * num[2]
    return money


if __name__ == '__main__':
    main()
