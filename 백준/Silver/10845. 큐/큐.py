N = int(input())
from collections import deque
dq = deque('')
for i in range(N):
    a = input()
    if a == 'pop':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif a == 'size':
        print(len(dq))
    elif a == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif a == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif a == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)
    else:
        push, val = a.split()
        dq.append(val)