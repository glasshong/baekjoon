N = int(input())
l = []
for _ in range(N):
    x, y = map(int, input().split())
    l.append([x, y])
l.sort()
for i in l:
    print(f'{i[0]} {i[1]}')