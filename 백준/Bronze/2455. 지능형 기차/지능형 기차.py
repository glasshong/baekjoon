a, b = map(int, input().split())
l = [b-a]
for i in range(1, 4):
    a, b = map(int, input().split())
    l.append(l[i-1]+b-a)
print(max(l))