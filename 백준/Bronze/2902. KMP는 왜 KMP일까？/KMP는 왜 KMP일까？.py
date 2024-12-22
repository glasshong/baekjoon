a = input()
l = a.split('-')
f = []
for i in range(len(l)):
    f.append(l[i][0])
print(*f, sep='')