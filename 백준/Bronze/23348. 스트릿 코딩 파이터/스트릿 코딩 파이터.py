a, b, c = map(int, input().split())
n = int(input())
answer = []

for _ in range(n):
    total = 0
    for _ in range(3):
        d, e, f = map(int, input().split())
        total += d * a + e * b + f * c
    answer.append(total)

print(max(answer))