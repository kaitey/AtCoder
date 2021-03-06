def main():
    n = int(input())
    A = list(map(int, input().split()))
    sn_s = 0
    sq_s = 0
    for a in A:
        sn_s += a
        sq_s += a ** 2
    print(sq_s * (n - 1) - 2 * (sn_s ** 2 - sq_s) // 2)


if __name__ == '__main__':
    main()
