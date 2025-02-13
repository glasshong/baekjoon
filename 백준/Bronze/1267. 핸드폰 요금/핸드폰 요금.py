N = int(input())
l = list(map(int, input().split()))

y = 0
m = 0
for i in l:
    y += 10 * ((i // 30) + 1)
    m += 15 * ((i // 60) + 1)

if y < m:
    print(f'Y {y}')
elif y > m:
    print(f'M {m}')
else:
    print(f'Y M {y}')