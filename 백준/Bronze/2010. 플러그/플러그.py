import sys
input = sys.stdin.readline

N = int(input())
a = 0
for _ in range(N):
    a += int(input())
print(a-N+1)