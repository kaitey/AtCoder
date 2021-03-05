def main():
    n = int(input())
    a = list(map(int, input().split(" ")))
    a.sort(reverse=True)
    print(cal_diff(a))


def cal_diff(lists):
    alice, bob = 0, 0
    for s in range(0, len(lists), 2):
        tmp = lists[s: s + 2] + [0]
        alice += tmp[0]
        bob += tmp[1]
    return alice - bob


if __name__ == '__main__':
    main()
