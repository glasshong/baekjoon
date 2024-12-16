T = int(input())
l = []
for _ in range(T):
    l = list(map(int, input().split()))
    e = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            e.append(l[i])
        else:
            pass
    print(sum(e), min(e))