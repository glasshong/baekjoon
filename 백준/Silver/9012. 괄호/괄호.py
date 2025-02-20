t = int(input())

for _ in range(t):
    s = list(input())
    stack = []

    for i in s:
        if stack == []:
            stack.append(i)
        elif stack[-1] == '(' and i == ')':
            stack.pop()
        else:
            stack.append(i)
    
    if stack == []:
        print('YES')
    else:
        print('NO')