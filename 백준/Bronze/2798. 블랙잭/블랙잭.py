N, M = map(int, input().split())
l = list(map(int, input().split()))
m = []
for i in range(len(l)):
    for j in range(i):
        for k in range(j):
            if l[i] + l[j] + l[k] <= M:
                m.append(l[i] + l[j] + l[k])
            else:
                pass
print(max(m))