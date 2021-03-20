from math import ceil


def main():
    n = int(input())
    n_len = len(str(n))
    h_n_len = ceil(n_len / 2)
    count = 10 ** (h_n_len - 1) - 1
    for i in range(10 ** (h_n_len - 1), 10 ** h_n_len):
        num = int(str(i) * 2)
        if num > n:
            break
        count += 1
    print(count)


if __name__ == '__main__':
    main()
