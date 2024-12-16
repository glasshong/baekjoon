l = []
for _ in range(9):
    l.append(int(input()))
a = []
for i in range(9):
    for j in range(i):
        if sum(l) - 100 == l[i] + l[j]:
            a.append(i)
            a.append(j)
l.remove(l[a[0]])
l.remove(l[a[1]])
print(*l, sep='\n')