from math import ceil


def main():
    x, y, z = list(map(int, input().split()))
    print(ceil(y * z / x - 1))


if __name__ == '__main__':
    main()
