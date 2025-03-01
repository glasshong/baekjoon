n = int(input())
l = []
for i in range(n):
    a, b, c, d = map(int, input().split())
    if a == b == c == d:
        l.append(50000 + a * 5000)
    elif a == b == c or a == b == d or a == c == d:
        l.append(10000 + a * 1000)
    elif b == c == d:
        l.append(10000 + b * 1000)
    elif (a == b and c == d) or (a == d and b == c):
        l.append(2000 + a * 500 + c * 500)
    elif a == c and b == d:
        l.append(2000 + a * 500 + b * 500)
    elif a == b or a == c or a == d:
        l.append(1000 + a * 100)
    elif b == c or b == d:
        l.append(1000 + b * 100)  
    elif c == d:
        l.append(1000 + c * 100)
    else:
        l.append(max(a, b, c, d) * 100)

print(max(l))