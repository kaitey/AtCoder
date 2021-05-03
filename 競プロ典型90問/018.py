from math import atan, sin, cos, sqrt, degrees, pi

T = int(input())
L, X, Y = list(map(int, input().split()))
XS = pow(X, 2)
Q = int(input())
for _ in range(Q):
    e = int(input())
    y = L * (1 - cos(2 * pi / T * e)) / 2
    x = sqrt(XS + pow(L * sin(2 * pi / T * e) / 2 + Y, 2))
    theta = atan(y / x)
    print(degrees(theta))
