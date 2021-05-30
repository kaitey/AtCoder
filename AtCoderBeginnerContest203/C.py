def main():
    N, K = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    money = K
    # new = 0
    for ab in AB:
        if ab[0] <= money:
            money += ab[1]
        else:
            print(money)
            exit()
    print(money)


if __name__ == '__main__':
    main()
