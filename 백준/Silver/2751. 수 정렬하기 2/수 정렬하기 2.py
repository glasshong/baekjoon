import sys
input = sys.stdin.readline

N = int(input().strip())
l = []
for _ in range(N):
    l.append(int(input()))
l.sort()
print(*l, sep='\n')