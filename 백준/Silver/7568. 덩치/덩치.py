n = int(input())
a = []
b = []

for _ in range(n):
    x, y = map(int, input().split())
    a.append((x, y))
   
for i in range(n):
    cnt = 0
    for j in range(n):
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            cnt += 1
    b.append(cnt + 1)

print(*b)
