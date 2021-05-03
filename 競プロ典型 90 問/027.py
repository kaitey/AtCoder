n = int(input())
d = dict()
for i in range(1, n + 1):
    s = input()
    try:
        if d[s] == 1:
            pass
    except KeyError:
        print(i)
        d[s] = 1
