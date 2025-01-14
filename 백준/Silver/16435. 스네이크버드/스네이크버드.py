N, L = map(int, input().split())
l = sorted(list(map(int, input().split())))
for i in l:
    if i <= L:
        L += 1
print(L)