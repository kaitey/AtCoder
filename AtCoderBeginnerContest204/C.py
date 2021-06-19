import sys
sys.setrecursionlimit(50000)


def dfs(graph, start):
    states[start] = True
    for u in graph[start]:
        if not states[u]:
            dfs(graph, u)


N, M = list(map(int, input().split()))
G = [set() for _ in range(N)]
for _ in range(M):
    tmp = list(map(int, input().split()))
    G[tmp[0] - 1].add(tmp[1] - 1)
ans = 0
for n in range(N):
    states = [False] * N
    dfs(G, n)
    ans += states.count(True)
print(ans)
