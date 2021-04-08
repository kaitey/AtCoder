from math import sin, cos, pi


def main():
    n = int(input())
    x0, y0 = list(map(int, input().split()))
    xn, yn = list(map(int, input().split()))
    xc, yc = (x0 + xn) / 2, (y0 + yn) / 2
    c0 = complex(x0, y0)
    cc = complex(xc, yc)
    ang = 2 * pi / n
    rot = complex(cos(ang), sin(ang))
    c1 = (c0 - cc) * rot + cc
    print(c1.real, c1.imag)


if __name__ == '__main__':
    main()
