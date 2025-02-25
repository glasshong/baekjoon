M = int(input())
N = int(input())
a = list(range(M, N+1))
b = []

if 1 in a:
    a.remove(1)

for i in a:
    for j in range(2, i):
        if i % j == 0:
            b.append(i)
            break

a = set(a)
b = set(b)
f = list(a-b)

if f == []:
    print(-1)
else:
    print(sum(f))
    print(min(f))