def main():
    n = int(input())
    A = list(map(int, input().split()))
    A = sorted(enumerate(A), key=lambda x: x[1])[:8]
    mods = dict()
    for i in range(1, 1 << len(A)):
        ids = []
        nums = 0
        for j, k in enumerate(reversed(bin(i)[2:])):
            if k == "1":
                ids.append(A[-j - 1][0] + 1)
                nums += A[-j - 1][1]
                ids.sort()
        mod = nums % 200
        if mod not in mods.keys():
            mods[mod] = ids
        else:
            print("Yes")
            print(len(mods[mod]), *mods[mod])
            print(len(ids), *ids)
            exit()
    print("No")


if __name__ == '__main__':
    main()
