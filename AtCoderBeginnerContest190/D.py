import math
from copy import deepcopy


def main():
    n = abs(int(input()))
    if n == 1:
        print("2")
        return

    is_even = True
    count = 0
    if n % 2 == 1:
        is_even = False
        fac, is_square = factorization((n - 1) // 2)
        div_num = clac_div_num(fac)
        count += (math.ceil(div_num / 2)) * 2

        fac, is_square = factorization(n)
        div_num = clac_div_num(fac)
        count += (math.ceil(div_num / 2)) * 2
    else:
        n_tmp = deepcopy(n)
        c = 0
        while True:
            if n_tmp % 2 == 0:
                c += 1
                n_tmp = n_tmp // 2
            else:
                break
        n_odd = n // (2 ** c)
        low, high = make_divisors(n_odd)
        big_divs = [s for s, b in zip(low, high) if b < s * (2 ** c)]
        big_divs += high
        count += 2 * len(big_divs)
    print(count)


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors, upper_divisors


def clac_div_num(facs):
    num = 1
    for n in facs:
        num *= n[1]
    return num


def factorization(n):
    arr = []
    temp = n
    is_square = True
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
            if is_square and cnt % 2 != 0:
                is_square = False

    if temp != 1:
        is_square = False
        arr.append([temp, 1])

    if not arr:
        is_square = False
        arr.append([n, 1])

    return arr, is_square


if __name__ == '__main__':
    main()
