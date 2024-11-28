n = int(input())
A = 100
B = 100

for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        B = B-a
    elif a < b:
        A = A-b
    else:
        pass

print(A)
print(B)