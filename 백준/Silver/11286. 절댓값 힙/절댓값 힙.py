import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []

for _ in range(N):
    a = int(input())
    if a == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(a), a))