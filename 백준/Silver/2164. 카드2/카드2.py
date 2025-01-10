N = int(input())

from collections import deque
queue = deque(range(1, N+1))
 
while len(queue) > 1:
    queue.popleft()
    queue.append(queue[0])
    queue.popleft()

print(*queue)