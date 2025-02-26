a, b = map(int, input().split())

l = []
for i in range(1000):
    l.extend([i] * i)

print(sum(l[a-1:b]))