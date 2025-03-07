n, m = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(m):
    a.sort()
    s = sum(a[:2])
    a[0] = s
    a[1] = s

print(sum(a))
