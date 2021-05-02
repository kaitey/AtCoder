def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = min(b) - max(a) + 1
    if ans <= 0:
        print("0")
    else:
        print(ans)


if __name__ == '__main__':
    main()
