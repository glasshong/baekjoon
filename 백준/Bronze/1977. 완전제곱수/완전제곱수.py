M = int(input())
N = int(input())
a = list(range(M, N+1))
b = []
for i in a:
    if (i ** 0.5) % 1 == 0:
        b.append(i)
if b == []:
    print(-1)
else:
    print(sum(b), min(b), sep='\n')