N = int(input())
l = []
for _ in range(N):
    l.append(input())
for i in range(N):
    print(f'{i+1}. {l[i]}')