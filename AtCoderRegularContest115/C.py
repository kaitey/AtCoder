def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def main():
    n = int(input())
    A = [-1] * n
    for i in range(n):
        A[i] = len(prime_factorize(i + 1)) + 1
    print(*A)


if __name__ == '__main__':
    main()
