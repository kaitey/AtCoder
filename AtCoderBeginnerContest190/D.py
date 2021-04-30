def main():
    n = int(input())
    while n % 2 == 0:
        n //= 2
    divs = make_divisors(n)
    print(len(divs) * 2)


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors


if __name__ == '__main__':
    main()
