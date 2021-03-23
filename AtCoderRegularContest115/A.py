def main():
    n, m = list(map(int, input().split()))
    even, odd = 0, 0
    for i in range(n):
        s_i = input()
        if s_i.count("1") % 2 == 1:
            odd += 1
        else:
            even += 1

    print(odd * even)


if __name__ == '__main__':
    main()
