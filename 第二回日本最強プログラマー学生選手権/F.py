def main():
    n, m, q = list(map(int, input().split()))
    A = [0] * n
    B = [0] * m
    s = 0
    for _ in range(q):
        t, x, y = list(map(int, input().split()))
        if t == 1:
            tmp = A[x - 1]
            A[x - 1] = y
            old = 0
            new = 0
            for b in B:
                old += tmp if tmp >= b else b
                new += y if y >= b else b
        else:
            tmp = B[x - 1]
            B[x - 1] = y
            old = 0
            new = 0
            for a in A:
                old += tmp if tmp >= a else a
                new += y if y >= a else a
        s = s - old + new
        print(s)


if __name__ == '__main__':
    main()
