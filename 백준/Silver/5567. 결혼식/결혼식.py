import sys
input = sys.stdin.readline

from collections import deque
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

v = [False] * (n+1)
v[1] = True

q = deque([1])
d = [0] * (n+1)

count = 0
while q:
    c = q.popleft()
    for i in graph[c]:
        if not v[i]:
            v[i] = True
            d[i] = d[c] + 1
            if d[i] <= 2:
                count += 1
                q.append(i)

print(count)