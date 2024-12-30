import sys
N, M = map(int, sys.stdin.readline().split())
l = {}
for _ in range(N):
    d, p = sys.stdin.readline().split()
    l[d] = p
for _ in range(M):
    print(l[sys.stdin.readline().strip()])