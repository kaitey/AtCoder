def calc_or_num(or_list):
    if not or_list:
        return 0
    or_num = or_list[0]
    for k in or_list[1:]:
        or_num = or_num | k
    return or_num


def main():
    n = int(input())
    a = list(map(int, input().split()))
    mini = 2 << 31
    for i in range(2 << (n-1)):
        xor_list = []
        or_list = []
        j = 0
        for j, m in enumerate(reversed(bin(i)[2:])):
            or_list.append(a[- j - 1])
            if m == "1":
                xor_list.append(calc_or_num(or_list))
                or_list = []
        or_list.extend(a[:- j - 1])
        xor_list.append(calc_or_num(or_list))
        xor_num = xor_list[0]
        for k in xor_list[1:]:
            xor_num = xor_num ^ k
        if xor_num < mini:
            mini = xor_num
    print(mini)


if __name__ == '__main__':
    main()
