def main():
    N, K = list(map(int, input().split()))
    ans = sum(range(N + 1)) * K * 100
    ans += sum(range(K + 1)) * N
    print(ans)


if __name__ == '__main__':
    main()
