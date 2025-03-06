n = int(input())
l = list(map(int, input().split()))
f = [0] * n

for i in range(n):
    c = l[i]
    for j in range(n):
        if f[j] == 0:
            if c == 0:
                f[j] = i+1
                break
            c -= 1

print(*f)