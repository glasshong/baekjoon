import sys
N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
l.sort()
s = 0
for i in range(N):
    s += l[i] * (N-i)
print(s)