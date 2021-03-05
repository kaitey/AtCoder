def main():
    s = input()
    num = 0
    twin = 0
    base = ""
    for i in range(2, len(s)):
        if s[i - 2] == s[i - 1] != s[i] and s[i-2] != base:
            base = s[i - 2]
            twin += 1
        num += twin
        if s[i] == base:
            num -= 1
    print(num)


if __name__ == '__main__':
    main()
