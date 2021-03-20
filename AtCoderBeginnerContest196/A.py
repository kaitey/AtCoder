def main():
    a, b = list(map(int, input().split()))
    c, d = list(map(int, input().split()))

    print(max(a, b) - min(c, d))


if __name__ == '__main__':
    main()
