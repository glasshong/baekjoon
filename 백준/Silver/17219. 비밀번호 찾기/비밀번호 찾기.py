N, M = map(int, input().split())
l = {}
for _ in range(N):
    d, p = input().split()
    l[d] = p
for _ in range(M):
    print(l[input()])