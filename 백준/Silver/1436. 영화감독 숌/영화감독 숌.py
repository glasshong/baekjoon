N = int(input())

n = 666
a = n

while N > 1:
    n += 1
    if '666' in str(n):
        a = n
        N -= 1

print(a)