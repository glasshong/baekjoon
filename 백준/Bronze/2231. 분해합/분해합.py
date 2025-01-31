N = int(input())

n = 0
a = n

while n != N:
    m = str(n)
    t = 0
    for i in range(len(m)):
        t += int(m[i])
    if t + n == N:
        a = n
        break
    else:
        n += 1

if a == N:
    print(0)
else:
    print(a)