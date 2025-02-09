a = list(map(int, input().split()))
b = [1, 1, 2, 2, 2, 8]
c = []

for i in range(6):
    if a[i] == b[i]:
        c.append(0)
    else:
        c.append(b[i]-a[i])

print(*c)