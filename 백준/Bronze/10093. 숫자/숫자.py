a, b = map(int, input().split())

if a > b:
    a, b = b, a

l = list(range(a+1, b))

print(len(l))
print(*l)