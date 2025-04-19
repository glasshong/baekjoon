import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
graph = [list(map(str, input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, color, graph):
    v[x][y] = True
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not v[nx][ny] and graph[nx][ny] == color:
                    v[nx][ny] = True
                    q.append((nx, ny))

v = [[False] * n for _ in range(n)]
c = ['R', 'G', 'B']
a1 = []
for color in c:
    count = 0
    for i in range(n):
        for j in range(n):
            if not v[i][j] and graph[i][j] == color:
                bfs(i, j, color, graph)
                count += 1
    a1.append(count)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

v = [[False] * n for _ in range(n)]
c = ['R', 'B']
a2 = []
for color in c:
    count = 0
    for i in range(n):
        for j in range(n):
            if not v[i][j] and graph[i][j] == color:
                bfs(i, j, color, graph)
                count += 1
    a2.append(count)

print(sum(a1), sum(a2))