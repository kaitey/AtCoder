def main():
    n, x = list(map(int, input().split()))
    aa = list(map(int, input().split()))
    aa_p = [a for a in aa if a != x]
    print(*aa_p)


if __name__ == '__main__':
    main()
