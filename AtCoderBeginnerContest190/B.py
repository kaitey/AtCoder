def main():
    n, s, d = list(map(int, input().split()))
    for i in range(n):
        x, y = list(map(int, input().split()))
        if x < s and y > d:
            print("Yes")
            return
    print("No")


if __name__ == '__main__':
    main()
