def main():
    n, m = list(map(int, input().split()))
    S = [0] * n
    for i in range(n):
        S[i] = int(input(), 2)

    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if bin(S[i] ^ S[j])[2:].count("1") % 2 == 1:
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
