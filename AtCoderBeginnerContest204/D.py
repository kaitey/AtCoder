N = int(input())
T = list(map(int, input().split()))
S = sum(T)
mid = -(-S // 2)
dp = [[False] * (S + 1) for _ in range(N)]
dp[0][0] = True
dp[0][T[0]] = True
for n in range(1, N):
    for s in range(S + 1):
        if dp[n - 1][s]:
            dp[n][s] = True
            dp[n][s + T[n]] = True
for s in range(mid, S + 1):
    if dp[-1][s]:
        print(s)
        exit()
