l = []
w = []
for _ in range(5):
    l = list(map(int, input().split()))
    w.append(sum(l))
m = max(w)
print(w.index(m)+1, m)