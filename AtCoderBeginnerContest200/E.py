def main():
    n, k = list(map(int, input().split()))
    dp = [set() for _ in range(n)]
    dp[0].add((1, 1, 1))
    cnt = 1
    for i in range(1, n):
        for d in dp[i-1]:
            if d[0] < n:
                dp[i].add((d[0] + 1, d[1], d[2]))
            if d[1] < n:
                dp[i].add((d[0], d[1] + 1, d[2]))
            if d[2] < n:
                dp[i].add((d[0], d[1], d[2] + 1))
        le = len(dp[i])
        if cnt + le >= k or i == n-1:
            li = list(dp[i])
            li.sort()
            print(*li[k-cnt-1])
            exit()
        cnt += le


if __name__ == '__main__':
    main()
