import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
a, b = map(int, input().split())

m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start, end, graph):
    q = deque()
    q.append(start)
    v = [-1] * (n+1)
    v[start] = 0

    while q:
        c = q.popleft()
        
        for i in graph[c]:
            if v[i] == -1:
                v[i] = v[c]+1
                q.append(i)
            if i == end:
                return v[i]

    return -1

print(bfs(a, b, graph))