def main():
    n = int(input())
    n_len = len(str(n))
    count = 0
    for i in range(1, n_len):
        count += ((i - 1) // 3) * (10 ** i - 10 ** (i - 1))
    count += ((n_len - 1) // 3) * (n - 10 ** (n_len - 1) + 1)
    print(count)


if __name__ == '__main__':
    main()
