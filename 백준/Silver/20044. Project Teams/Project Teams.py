n = int(input())
l = list(map(int, input().split()))
l.sort()

answer = []
for i in range(len(l)):
    answer.append(l[i] + l[len(l)-i-1])

print(min(answer))