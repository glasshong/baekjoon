import sys
input = sys.stdin.readline

from collections import deque

dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(x, y, graph):
    q = deque([(x, y)])
    v[x][y] = True
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if not v[nx][ny] and graph[nx][ny] == 1:
                    v[nx][ny] = True
                    q.append((nx, ny))
                    count += 1

    return count

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
        
    v = [[False]* w for _ in range(h)]
        
    answer = []
    for i in range(h):
        for j in range(w):
            if not v[i][j] and graph[i][j] == 1:
                answer.append(bfs(i, j, graph))
    
    print(len(answer))