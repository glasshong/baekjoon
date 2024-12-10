t = 0
l = []
for i in range(4):
    a, b = map(int, input().split())
    t -= a
    t += b
    l.append(t)
print(max(l))