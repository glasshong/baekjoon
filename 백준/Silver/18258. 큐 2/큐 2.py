import sys
from collections import deque
input = sys.stdin.readline
q = deque()
n = int(input())

for _ in range(n):
    a = input().rstrip()
    if a == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif a == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    elif a == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif a == 'size':
        print(len(q))
    elif a == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    else:
        b, c = a.split()
        q.append(int(c))