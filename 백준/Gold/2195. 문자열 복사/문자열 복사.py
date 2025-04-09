s = input()
p = input()

a = 0
count = 0

while a < len(p):
    b = 0
    for i in range(1, len(p)-a+1):
        if p[a:a+i] in s:
            b = i
        else:
            break
    count += 1
    a += b

print(count)