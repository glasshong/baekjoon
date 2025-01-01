import sys
N, M = map(int, sys.stdin.readline().strip().split())
l = []
l_d = {}
for i in range(N):
    a = sys.stdin.readline().strip()
    l.append(a)
    l_d[a] = i+1

for _ in range(M):
    b = sys.stdin.readline().strip()
    if b in l_d:
        print(l_d[b])
    else:
        print(l[int(b)-1])