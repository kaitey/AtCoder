def main():
    n = input()
    if n == n[::-1]:
        print("Yes")
        return
    while n[-1] == "0":
        if n[:-1] == n[:-1][::-1]:
            print("Yes")
            return
        n = n[:-1]
    print("No")


if __name__ == '__main__':
    main()
