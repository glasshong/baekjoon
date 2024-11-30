a = []
b = []
for _ in range(3):
    c, d = map(int, input().split())
    if c in a:
        a.remove(c)
    else:
        a.append(c) 
    if d in b:
        b.remove(d)
    else:
        b.append(d) 
print(a[0], b[0])