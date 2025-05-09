import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(x, y, h, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(x, y)])
    v[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not v[nx][ny] and graph[nx][ny] > h:
                    v[nx][ny] = True
                    q.append((nx, ny))

answer = 0
for h in range(0, 101):
    v = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not v[i][j] and graph[i][j] > h:
                bfs(i, j, h, graph)
                count += 1
    answer = max(answer, count)

print(answer)