n = int(input())
CP = [list(map(int, input().split())) for _ in range(n)]
S = [[0] * 2 for _ in range(n)]
for i, cp in enumerate(CP):
    S[i] = [S[i-1][0], S[i-1][1]]
    S[i][cp[0]-1] += cp[1]

q = int(input())
for _ in range(q):
    l, r = list(map(int, input().split()))
    if l >= 2:
        print(S[r-1][0]-S[l-2][0], S[r-1][1]-S[l-2][1])
    else:
        print(S[r-1][0], S[r-1][1])
