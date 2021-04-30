def main():
    n, m = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    ans = list(a ^ b)
    ans.sort()
    print(*ans)


if __name__ == '__main__':
    main()
