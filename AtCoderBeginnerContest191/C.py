def main():
    h, w = list(map(int, input().split()))
    S = [input() for _ in range(h)]
    num = 0
    for i in range(1, h):
        for j in range(1, w):
            if (S[i-1][j-1], S[i][j-1], S[i - 1][j], S[i][j]).count("#") % 2 != 0:
                num += 1
    print(num)


if __name__ == '__main__':
    main()
