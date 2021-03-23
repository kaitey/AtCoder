def main():
    n = int(input())
    A = [-1] * n
    A[0] = 1
    i = 1
    while i < n:
        if A[i] == -1:
            A[i] = 2
            for j in range(2, n // (i + 1) + 1):
                if A[(i + 1) * j - 1] == -1:
                    A[(i + 1) * j - 1] = j + 1
        i += 1
    print(*A)


if __name__ == '__main__':
    main()
