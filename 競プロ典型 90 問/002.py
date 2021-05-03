from math import ceil

n = int(input())
if n % 2 == 1:
    exit()
strs = [set() for _ in range(n // 2)]
strs[0].add('()')
for i in range(1, n // 2):
    for a in strs[i - 1]:
        strs[i].add(''.join(('(', a, ')')))
    for j in range(ceil((i + 1) / 2)):
        for a in strs[j]:
            for b in strs[i - j - 1]:
                strs[i].add(''.join((a, b)))
                strs[i].add(''.join((b, a)))
ans = list(strs[-1])
ans.sort()
for a in ans:
    print(a)
