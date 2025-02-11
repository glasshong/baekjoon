l = []
for i in range(8):
    l.append(int(input()))
sort_l = sorted(l)
a = sort_l[3:]
print(sum(a))

i = []
for j in range(5):
    i.append(l.index(a[j])+1)

b = sorted(i)
print(*b)