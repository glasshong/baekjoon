N = int(input())
l = []
for _ in range(N):
    x, y = map(int, input().split())
    l.append([x, y])
l_sort = sorted(l, key=lambda x:(x[1], x[0]))
for i in l_sort:
    print(f'{i[0]} {i[1]}')