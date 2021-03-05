def main():
    t = int(input())
    for i in range(t):
        l, r = list(map(int, input().split(" ")))
        most = r - l
        if most < l:
            print("0")
            continue
        aa = most - l + 1
        print(aa * (aa + 1) // 2)


if __name__ == '__main__':
    main()
