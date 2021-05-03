n = int(input())
A, B, C = list(map(int, input().split()))
L = 9999
ans = 9999
for x in range(L + 1):
    for y in range(L - x + 1):
        if n - A * x - B * y >= 0 and (n - A * x - B * y) % C == 0:
            tmp = (n - A * x - B * y) // C + x + y
            if tmp < ans:
                ans = tmp
print(ans)
