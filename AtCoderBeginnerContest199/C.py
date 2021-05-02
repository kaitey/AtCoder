def main():
    n = int(input())
    s = list(input())
    q = int(input())
    flip = 0
    for _ in range(q):
        t, a, b = list(map(int, input().split()))
        if t == 1:
            ap = (a + flip * n) % (2 * n)
            bp = (b + flip * n) % (2 * n)
            s[ap - 1], s[bp - 1] = s[bp - 1], s[ap - 1]
        else:
            flip += 1
    if flip % 2 == 1:
        s[:n], s[n:] = s[n:], s[:n]
    print(''.join(s))


if __name__ == '__main__':
    main()
