from math import gcd

a, b = list(map(int, input().split()))
lcm = a * b // gcd(a, b)
if lcm > pow(10, 18):
  print("Large")
else:
  print(lcm)
