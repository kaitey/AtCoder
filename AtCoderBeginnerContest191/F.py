def main():
    n = int(input())
    a = (list(map(int, input().split(" ")))) * 2
    tmp_b = [m % n for m in a]
    for k in range(n):
        b = tmp_b[k:k+n]
        calc_inv_num(b)


def calc_inv_num(b):
    counter = [int(b[i] > b[j]) for i in range(0, len(b)) for j in range(i + 1, len(b))]
    print(sum(counter))


if __name__ == '__main__':
    main()
