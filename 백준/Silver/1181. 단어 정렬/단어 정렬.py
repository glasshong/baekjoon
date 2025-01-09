N = int(input())
l = {}

for _ in range(N):
    a = input() 
    b = len(a)
    if b not in l:
        l[b] = []
    l[b].append(a)

for k in l:
    l[k] = sorted(set(l[k]))

s = dict(sorted(l.items(), key=lambda x: x[0]))

for k, ws in s.items():
    for w in ws:
        print(w)