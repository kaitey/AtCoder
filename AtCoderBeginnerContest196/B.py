def main():
    s = input()
    if "." in s:
        s = s[:s.index(".")]
    print(s)


if __name__ == '__main__':
    main()
