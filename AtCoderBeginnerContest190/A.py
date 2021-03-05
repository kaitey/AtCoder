def main():
    a, b, c = list(map(int, input().split()))
    if a > b or (a == b and c == 1):
        print("Takahashi")
    else :
        print("Aoki")


if __name__ == '__main__':
    main()
