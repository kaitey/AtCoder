def main():
    n = int(input())
    i = 2
    passes = []
    while True:
        tmp = int((n + 1) ** (1 / i))
        if tmp == 1:
            break
        tmp_pass = [j ** i for j in range(2, tmp + 1) if j ** i <= n]
        passes.extend(tmp_pass)
        i += 1
    print(n - len(set(passes)))


if __name__ == '__main__':
    main()
