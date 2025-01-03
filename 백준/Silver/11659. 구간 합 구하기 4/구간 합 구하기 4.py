import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
l = list(map(int, input().rstrip().split()))
a = 0
w = []
for i in range(N):
    a += l[i]
    w.append(a)
for _ in range(M):
    i, j = map(int, input().rstrip().split()) 
    if i == 1:
        print(w[j-1])
    else:
        print(w[j-1]-w[i-2])