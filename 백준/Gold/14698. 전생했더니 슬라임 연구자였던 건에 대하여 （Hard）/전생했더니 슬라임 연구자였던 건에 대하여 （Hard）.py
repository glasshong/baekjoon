import sys
import heapq

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    hq = []

    for i in l:
        heapq.heappush(hq, i)
    
    total = 1
    for _ in range(n-1):
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        total *= (a * b)
        heapq.heappush(hq, a * b)
    
    if n == 1:
        print(1)
    else:
        print(total % 1000000007)