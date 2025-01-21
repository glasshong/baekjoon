t = []
a = []

for _ in range(5):
    a.append(input())

for i in range(5):
    if 'FBI' in a[i]:
        t.append(i+1)

if t == []:
    print('HE GOT AWAY!')
else:
    print(*t)