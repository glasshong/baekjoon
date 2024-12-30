import sys
N, M = map(int, sys.stdin.readline().split())

a = set()
for _ in range(N):
    a.add(sys.stdin.readline().strip())

b = set()
for _ in range(M):
    b.add(sys.stdin.readline().strip())

u = sorted(list(a & b))

print(len(u))
print(*u, sep='\n')