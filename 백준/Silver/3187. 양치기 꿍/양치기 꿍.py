import sys
input = sys.stdin.readline

from collections import deque

r, c = map(int, input().split())

graph = []
for _ in range(r):
    l = list(map(str, input().strip()))
    graph.append(l)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

v = [[False] * (c) for _ in range(r)]

def bfs(x, y, graph):
    q = deque([(x, y)])
    v[x][y] = True
    cnt_k = 0 # 양
    cnt_v = 0 # 늑대
    
    if graph[x][y] == 'k':
        cnt_k += 1
    elif graph[x][y] == 'v':
        cnt_v += 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if v[nx][ny] or graph[nx][ny] == '#':
                    continue
                v[nx][ny] = True
                q.append((nx, ny))
                if graph[nx][ny] == 'k':
                    cnt_k += 1
                elif graph[nx][ny] == 'v':
                    cnt_v += 1
    
    if cnt_k > cnt_v:
        cnt_v = 0    
    else:
        cnt_k = 0
    return cnt_k, cnt_v

answer = []
for i in range(r):
    for j in range(c):
        if not v[i][j] and graph[i][j] != '#':
            answer.append(bfs(i, j, graph))

print(sum(x for x, y in answer), sum(y for x, y in answer))