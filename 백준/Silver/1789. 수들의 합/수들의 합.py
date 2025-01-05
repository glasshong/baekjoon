S = int(input())
a = 0
b = 0
while True:
    b += 1
    a += b
    if a > S:
        break
print(b-1)