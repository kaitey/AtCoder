def main():
    a, b = list(map(int, input().split(" ")))
    r = (a * b) % 2
    if r == 0:
        print("Even")
    else:
        print("Odd")


if __name__ == '__main__':
    main()
