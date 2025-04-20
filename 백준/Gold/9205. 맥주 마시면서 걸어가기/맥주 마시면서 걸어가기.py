import sys
input = sys.stdin.readline

from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    p = []
    for _ in range(n+2):
        x, y = map(int, input().split())
        p.append((x, y))
    
    v = [False] * (n+2)
    q = deque([0])
    
    while q:
        c = q.popleft()
        
        for i in range(n+2):
            if not v[i]:
                if abs(p[i][0]-p[c][0]) + abs(p[i][1]-p[c][1]) <= 1000:
                    v[i] = True
                    q.append(i)
    if v[-1]:
        print('happy')
    else:
        print('sad')