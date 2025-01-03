import sys
input = sys.stdin.readline
N, M = map(int, input().split())
l = list(map(int, input().split()))
a = 0
w = [0]
for i in l:
    a += i
    w.append(a)
for _ in range(M):
    i, j = map(int, input().split())
    print(w[j]-w[i-1])