def main():
    s = input()
    for i in range(0, len(s), 2):
        try:
            if not (s[i].islower() and s[i+1].isupper()):
                print("No")
                return
        except IndexError:
            if not (s[i].islower()):
                print("No")
                return
    print("Yes")


if __name__ == '__main__':
    main()
