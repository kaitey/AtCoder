def main():
    N = int(input())
    ans = (((N - 1) / N) ** N) * 2 * N * N
    ans -= (((N - 2) / N) ** N) * 3 * N * N / 4
    print(ans / N)


if __name__ == '__main__':
    main()
