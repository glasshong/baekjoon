N, X = map(int, input().split())
l = []

a = list(map(int, input().split()))
for i in range(N):
    if a[i] < X:
        l.append(a[i])
print(*l)