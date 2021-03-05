def main():
    n, k = input().split(" ")
    k = int(k)
    num = int(n)
    for i in range(k):
        target_num_asc = int(''.join(sorted(n)))
        target_num_desc = int(''.join(sorted(n, reverse=True)))
        new_num = target_num_desc - target_num_asc
        if new_num == num:
            print(new_num)
            return
        num = new_num
        n = str(num)
    print(n)


if __name__ == '__main__':
    main()
