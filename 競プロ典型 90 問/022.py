from math import gcd

a, b, c = list(map(int, input().split()))
g = gcd(gcd(a, b), c)
ans = a // g + b // g + c // g - 3
print(ans)
