from copy import deepcopy


def main():
    n = int(input())
    aa = [[10001, -1], [10001, -1]]
    bb = [[10001, -1], [10001, -1]]
    for i in range(n):
        a, b = list(map(int, input().split()))
        if a <= aa[0][0]:
            aa[1] = deepcopy(aa[0])
            aa[0] = [a, i]
        elif aa[0][0] < a <= aa[1][0]:
            aa[1] = [a, i]
        if b <= bb[0][0]:
            bb[1] = deepcopy(bb[0])
            bb[0] = [b, i]
        elif bb[0][0] < b <= bb[1][0]:
            bb[1] = [b, i]
    if aa[0][1] != bb[0][1]:
        print(max(aa[0][0], bb[0][0]))
    else:
        print(min(min(max(aa[0][0], bb[1][0]), max(aa[1][0], bb[0][0])), aa[0][0] + bb[0][0]))


if __name__ == '__main__':
    main()
