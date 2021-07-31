def main():
    N = int(input())
    s = 0
    for i in range(1, N):
        s += i
        if s >= N:
            print(i)
            exit()


if __name__ == '__main__':
    main()
