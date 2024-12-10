p = 0
t = []
for _ in range(10):
    a, b = map(int, input().split())
    p -= a
    p += b
    t.append(p)
print(max(t))