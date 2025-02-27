T = int(input())

for _ in range(T):
    n = int(input())
    b = bin(n)[2:]
    l = len(b)
    f = []
    for i in range(len(b)):
        if b[int(l)-int(i)-1] == '1':
            f.append(i)
    print(*f)