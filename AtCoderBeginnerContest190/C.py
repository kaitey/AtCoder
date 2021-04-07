def main():
    n, m = list(map(int, input().split()))
    ab_s = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cds = [list(map(int, input().split())) for _ in range(k)]
    ans = 0
    for i in range(1 << k):
        dish = [0] * n
        num = "0" * k + bin(i)[2:]
        cnt = 0
        for j, cd in enumerate(reversed(cds)):
            dish[cd[int(num[- j - 1])] - 1] += 1
        for ab in ab_s:
            if dish[ab[0] - 1] >= 1 and dish[ab[1] - 1] >= 1:
                cnt += 1
        ans = max(ans, cnt)
    print(ans)


if __name__ == '__main__':
    main()
