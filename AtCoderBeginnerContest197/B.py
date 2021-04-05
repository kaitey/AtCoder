def main():
    h, w, x, y = list(map(int, input().split()))
    s = [input() for _ in range(h)]
    cnt = 1
    for i in range(x - 2, -1, -1):
        if s[i][y - 1] == "#":
            break
        cnt += 1
    for i in range(x, h):
        if s[i][y - 1] == "#":
            break
        cnt += 1
    for i in range(y - 2, -1, -1):
        if s[x - 1][i] == "#":
            break
        cnt += 1
    for i in range(y, w):
        if s[x - 1][i] == "#":
            break
        cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
