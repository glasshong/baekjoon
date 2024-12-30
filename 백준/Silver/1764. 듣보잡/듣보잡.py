N, M = map(int, input().split())

a = set()
for _ in range(N):
    a.add(input())

b = set()
for _ in range(M):
    b.add(input())

u = sorted(list(a & b))

print(len(u))
print(*u, sep='\n')