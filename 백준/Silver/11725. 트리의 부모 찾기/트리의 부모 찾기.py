import sys
input = sys.stdin.readline

from collections import deque
n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n+1)

def bfs(root):
    q = deque([root])
    v = [False] * (n+1)
    v[root] = True
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not v[i]:
                v[i] = True
                parent[i] = node
                q.append(i)

bfs(1)
for i in parent[2:]:
    print(i)