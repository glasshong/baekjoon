t = int(input())
changes = [25, 10, 5, 1]

for _ in range(t):
    c = int(input())
    answer = []
    for i in changes:
        answer.append(c // i)
        c = c % i
    print(*answer)