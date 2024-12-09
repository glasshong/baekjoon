N, K = map(int, input().split())
l = []
for i in range(N):
    if N % (i+1) == 0:
        l.append(i+1)
if len(l) < K:
    print(0)
else:
    print(l[K-1])