from itertools import permutations

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
if N == 1:
    print(A[0][0])
    exit()
M = int(input())
bad = [set() for _ in range(N)]
for _ in range(M):
    XY = list(map(int, input().split()))
    bad[XY[0] - 1].add(XY[1] - 1)
    bad[XY[1] - 1].add(XY[0] - 1)
ans = 1001 * N
for V in permutations(range(N), N):
    if V[1] in bad[V[0]] or V[-2] in bad[V[-1]]:
        continue
    t = A[V[0]][0] + A[V[-1]][-1]
    bad_relay = False
    for i in range(1, N - 1):
        if {V[i - 1], V[i + 1]} & bad[V[i]]:
            bad_relay = True
            break
        t += A[V[i]][i]
    if bad_relay:
        continue
    if t < ans:
        ans = t
if ans > 1000 * N:
    print("-1")
else:
    print(ans)
