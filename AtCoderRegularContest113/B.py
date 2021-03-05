def main():
    a, b, c = list(map(int, input().split(" ")))
    a_mod10 = a % 10
    if a_mod10 in {0, 1, 5, 6}:
        print(a_mod10)
        return
    if a_mod10 in {4, 9}:
        if b % 2 == 1:
            print(a_mod10)
        else:
            print((a_mod10 ** 2) % 10)
        return
    b_mod4 = b % 4
    if b_mod4 == 0:
        print((a_mod10 ** 4) % 10)
    elif b_mod4 == 1:
        print(a_mod10)
    elif b_mod4 == 2:
        if c == 1:
            print((a_mod10 ** 2) % 10)
        else:
            print((a_mod10 ** 4) % 10)
    else:
        c_mod2 = c % 2
        if c_mod2 == 1:
            print((a_mod10 ** 3) % 10)
        else:
            print(a_mod10)


if __name__ == '__main__':
    main()
