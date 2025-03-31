t = int(input())
l = list(map(int, input().split()))

answer = 0
for i in l:
    if i == t:
        answer += 1
        
print(answer)