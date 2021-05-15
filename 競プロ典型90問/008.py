N = int(input())
S = input()
mod = 1000000007
dp = [[0] * 8 for _ in range(N + 1)]

dp[0][0] = 1
for i in range(N):
    for j in range(8):
        dp[i + 1][j] += dp[i][j]
        if (S[i], j) in {('a', 0), ('t', 1), ('c', 2), ('o', 3), ('d', 4), ('e', 5), ('r', 6)}:
            dp[i + 1][j + 1] += dp[i][j]
    for j in range(8):
        dp[i + 1][j] %= mod
print(dp[N][7] % mod)
