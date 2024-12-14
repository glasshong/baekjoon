l = []
d = []
for _ in range(9):
    l.append(int(input()))
for i in range(len(l)):
    for j in range(i):
        if l[i] + l[j] == sum(l) - 100:
            d.append(i)
            d.append(j)
del l[d[0]]
del l[d[1]]
l.sort()
print(*l, sep="\n")