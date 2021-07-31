from collections import Counter

N = int(input())
A = list(map(int, input().split()))
ans = N * (N - 1)
for v in Counter(A).values():
    ans -= v * (v - 1)
print(ans // 2)
