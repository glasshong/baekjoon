n = int(input())
l = list(map(int, input().split()))

t = 0
if l[0] == 1:
    t += 1

s = 1
for i in range(1, n):
    if l[i] == 1:
        if l[i-1] == 1:
            s += 1
            t += s
        else:
            t += 1
    else:
        s = 1

print(t)