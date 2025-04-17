import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

v = [[False]*m for _ in range(n)]

def bfs(x, y, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(x, y)])
    v[x][y] = True
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not v[nx][ny] and graph[nx][ny] == 1:
                    v[nx][ny] = True
                    q.append((nx, ny))
                    count += 1
    
    return count

answer = []
for i in range(n):
    for j in range(m):
        if not v[i][j] and graph[i][j] == 1:
            answer.append(bfs(i, j, graph))

print(len(answer))
print(max(answer) if answer else 0)