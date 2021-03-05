def main():
    n = int(input())
    d = [0] * n
    for i in range(n):
        d[i] = int(input())
    d = set(d)
    print(len(d))


if __name__ == '__main__':
    main()
