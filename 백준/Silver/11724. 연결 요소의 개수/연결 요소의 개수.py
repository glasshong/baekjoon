import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

v = [False] * (n+1)

def dfs(i):
    v[i] = True
    for j in graph[i]:
        if not v[j]:
            dfs(j)

count = 0
for i in range(1, n+1):
    if not v[i]:
        dfs(i)
        count += 1

print(count)