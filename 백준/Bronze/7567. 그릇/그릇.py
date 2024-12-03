a = list(input())
b = 10
for i in range(1, len(a)):
    if a[i-1] == '(':
        if a[i] == '(':
            b += 5
        else:
            b += 10
    elif a[i-1] == ')':
        if a[i] == ')':
            b += 5
        else:
            b += 10
print(b)