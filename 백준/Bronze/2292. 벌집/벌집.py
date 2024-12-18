N = int(input())
a = 1
i = 1
while True:
    if N <= a:
        break
    else:
        a += 6*i
        i += 1
print(i)