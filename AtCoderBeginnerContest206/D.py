import sys
sys.setrecursionlimit(10000000)


def get_num(key):
    try:
        return get_num(ch[key])
    except KeyError:
        return key


# N = int(input())
# A = list(map(int, input().split()))
N = 2 * pow(10, 5)
A = [i for i in range(1, N // 2 + 1)] * 2
ch = dict()
for i in range(N // 2):
    a, b = get_num(A[i]), get_num(A[N - 1 - i])
    if a != b:
        ch[b] = a

print(len(ch))
