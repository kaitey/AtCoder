from math import log, ceil


def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)


def main():
    x = input()
    m = int(input())
    d = int(max(x))
    max_d = d

    order = ceil(log(m, d))
    while order > len(x) or (order == len(x) and (m // (d ** order)) >= int(x[0])):
        (m // (d ** order))
        if order == len(x) and (m // (d ** order)) == int(x[0]):
            if int(Base_10_to_n(m, d)) < int(x):
                break
        max_d += 1
        order = ceil(log(m, max_d))
    print(max_d)
    print(max_d - d)


if __name__ == '__main__':
    main()



# def base_n_2_10(value, n):
#     if n <= 36:
#         return int(value, n)
#     base10 = 0
#     for i, v in enumerate(reversed(value)):
#         base10 += int(v) * (n ** i)
#     return base10
#
#
# def main():
#     x = input()
#     m = int(input())
#     x_str = str(x)
#     d = int(max(x_str))
#
#     cnt = 0
#     while True:
#         d += 1
#         aa = base_n_2_10(x, d)
#         if aa <= m:
#             cnt += 1
#         else:
#             print(cnt)
#             return
#
#
# if __name__ == '__main__':
#     main()

