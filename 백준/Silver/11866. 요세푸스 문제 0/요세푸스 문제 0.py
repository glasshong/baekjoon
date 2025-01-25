import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

l = list(range(1, n+1))
q = deque(l)

print('<', end = '')

for i in range(n):
    q.rotate(-k+1)
    if i == n-1: 
        print(q.popleft(), end = '')
    else:
        print(q.popleft(), end = ', ')

print('>')