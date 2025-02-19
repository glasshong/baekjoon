n = int(input())
cnt = 0

for _ in range(n):
    stack = []
    w = input()
    for i in range(0, len(w)):
        if stack and stack[-1] == w[i]:
            stack.pop()
        else:
            stack.append(w[i])
    if stack == []:
        cnt += 1

print(cnt)