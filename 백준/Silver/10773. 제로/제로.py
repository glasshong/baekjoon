K = int(input())
l = []
for i in range(K):
    n = int(input())
    if n == 0:
        l.pop()
    else:
        l.append(n)
print(sum(l))