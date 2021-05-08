def main():
    n = int(input())
    A = list(map(int, input().split()))
    mods = [[] for _ in range(200)]
    for a in A:
        mods[a % 200].append(a)
    cnt = 0
    for m in mods:
        l = len(m)
        if l >= 2:
            cnt += (l * (l - 1) // 2)
    print(cnt)


if __name__ == '__main__':
    main()
