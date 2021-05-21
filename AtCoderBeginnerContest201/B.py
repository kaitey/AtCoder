def main():
    n = int(input())
    ST = []
    for _ in range(n):
        tmp = input().split()
        tmp[1] = int(tmp[1])
        ST.append(tmp)
    ST.sort(key=lambda x: x[1], reverse=True)
    print(ST[1][0])


if __name__ == '__main__':
    main()
