T = int(input())
for _ in range(T):
    l = list(input().split())
    a = float(l[0]) 
    for i in range(1, len(l)):
        if l[i] == '@':
            a *= 3
        elif l[i] == '%':
            a += 5
        else:
            a -= 7
    print(f'{a:.2f}')