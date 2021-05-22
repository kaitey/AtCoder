from math import factorial


def main():
    A, B, K = list(map(int, input().split()))
    ans = ''
    while A * B != 0:
        mid = factorial(A + B - 1) // (factorial(A - 1) * factorial(B))
        if K <= mid:
            ans = ''.join((ans, 'a'))
            A -= 1
        else:
            ans = ''.join((ans, 'b'))
            K -= mid
            B -= 1
    if A == 0:
        ans = ''.join((ans, 'b' * B))
    else:
        ans = ''.join((ans, 'a' * A))
    print(ans)


if __name__ == '__main__':
    main()
