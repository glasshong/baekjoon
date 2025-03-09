import sys
import heapq

input = sys.stdin.readline

n = int(input())
hp = []
for _ in range(n):
    heapq.heappush(hp, int(input()))

answer = 0
for _ in range(n-1):
    a = heapq.heappop(hp)
    b = heapq.heappop(hp)
    answer += (a+b)
    heapq.heappush(hp, a+b)

print(answer)