def main():
    k = int(input())
    num = 0

    for a in range(1, k + 1):
        for b in range(a, k + 1):
            c_max = k // (a * b)
            if c_max == 0:
                break
            if a == b:
                num += c_max
            else:
                num += 2 * c_max
    print(num)


if __name__ == '__main__':
    main()
