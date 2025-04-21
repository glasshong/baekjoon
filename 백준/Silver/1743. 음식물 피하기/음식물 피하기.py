import sys
input = sys.stdin.readline

from collections import deque

n, m, k = map(int, input().split())

graph = [[0] * (m+1) for _ in range(n+1)]
for i in range(k):
    r, c = map(int, input().split())
    graph[r][c] = 1

v = [[False] * (m+1) for _ in range(n+1)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, graph):
    q = deque([(x, y)])
    v[x][y] = True
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 1 <= nx < n+1 and 1 <= ny < m+1:
                if not v[nx][ny] and graph[nx][ny] == 1:
                    v[nx][ny] = True
                    q.append((nx, ny))
                    count += 1
    return count

answer = []
for i in range(1, n+1):
    for j in range(1, m+1):
        if not v[i][j] and graph[i][j] == 1:
            answer.append(bfs(i, j, graph))

print(max(answer))