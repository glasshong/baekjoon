T = int(input())
a, b, c = 0, 0, 0

if T % 10 != 0:
    print(-1)
else:
    if T >= 300:
        a = T // 300
        T %= 300*a
    if T >= 60:
        b = T // 60
        T %= 60*b
    if T >= 10:
        c = T // 10
        T %= 10*c
    print(a, b, c)