l = [int(input()) for _ in range(7)]
a = 0
b = []
for i in range(7):
    if l[i] % 2 != 0:
        a += 1
        b.append(l[i])
    else:
        pass
if a == 0:
    print(-1)
else:
    print(sum(b))
    print(min(b))