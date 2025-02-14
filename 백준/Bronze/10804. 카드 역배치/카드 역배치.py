l = list(range(1, 21))

for _ in range(10):
    a, b = map(int, input().split())
    l = l[0:a-1] + list(reversed(l[a-1:b])) + l[b:20]

print(*l)