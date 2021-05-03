h, w = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(h)]
r_sum = [0] * h
c_sum = [0] * w
for i in range(h):
    for j in range(w):
        r_sum[i] += A[i][j]
        c_sum[j] += A[i][j]
ans = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        ans[i][j] = r_sum[i] + c_sum[j] - A[i][j]
for a in ans:
    print(*a)
