import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    l = list(map(int, input().strip()))
    graph.append(l)

def bfs(start_x, start_y, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(start_x, start_y)])
    v = set([(start_x, start_y)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if (nx, ny) not in v:
                    if graph[nx][ny] == 1:
                        v.add((nx, ny))
                        q.append((nx, ny))
                        graph[nx][ny] = graph[x][y] + 1
    
                        if nx == len(graph)-1 and ny == len(graph[0])-1:
                            return graph[nx][ny]

print(bfs(0, 0, graph))