from collections import deque
from itertools import islice
from statistics import median_low

N, K = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
list = deque()
ex = list.extend
mini = 1000000000
for i in range(N - K + 1):
    list.clear()
    for j in range(K):
        ex(A[j][i: i + K])
    med = median_low(list)
    if med < mini:
        mini = med
    for j in range(K, N):
        list = deque(islice(list, K, len(list)))
        ex(A[j][i: i + K])
        med = median_low(list)
        if med < mini:
            mini = med
print(mini)
