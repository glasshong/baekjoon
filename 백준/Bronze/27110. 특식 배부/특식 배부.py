n = int(input())
l = list(map(int, input().split()))

total = 0
for i in l:
    if i >= n:
        total += n
    else:
        total += i

print(total)