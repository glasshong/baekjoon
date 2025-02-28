N = int(input())
for i in range(N):
    a, b = map(str, input().split())
    la = sorted(list(a))
    lb = sorted(list(b))
    t = 0
    for i in range(len(la)):
        if la[i] != lb[i]:
            print('Impossible')
            break
        else:
            t += 1
    if t == len(la):
        print('Possible')