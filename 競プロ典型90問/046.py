N = int(input())
A = [0] * 46
B = [0] * 46
C = [0] * 46
A_tmp = list(map(lambda x: int(x) % 46, input().split()))
B_tmp = list(map(lambda x: int(x) % 46, input().split()))
C_tmp = list(map(lambda x: int(x) % 46, input().split()))
for i in range(46):
    A[i] = A_tmp.count(i)
    B[i] = B_tmp.count(i)
    C[i] = C_tmp.count(i)
ans = 0
for i in range(46):
    if A[i] == 0:
        continue
    for j in range(46):
        ans += (A[i] * B[j] * C[(- i - j) % 46])
print(ans)
