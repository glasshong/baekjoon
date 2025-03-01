w = list(input())
a = []
for i in w:
    a.append(i.lower())
s = set(a)
l = []

for i in s:
    l.append(a.count(i))
s = list(s)

if l.count(max(l)) >= 2:
    print('?')
else:
    f = l.index(max(l))
    print(s[f].upper())