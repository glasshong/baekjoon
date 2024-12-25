N = int(input())
l = []
for _ in range(N):
    x, y = input().split()
    l.append([int(x), y])
for i in sorted(l, key=lambda x: x[0]):
    print(i[0], i[1])