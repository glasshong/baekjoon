import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sungjoon = []

for _ in range(n):
    p, l = map(int, input().split())
    others = sorted(list(map(int, input().split())), reverse = True)
    if p < l:
        sungjoon.append(1)
    else:
        sungjoon.append(others[l-1])
    
sungjoon_sorted = sorted(sungjoon)

number = 0
total = 0
for i in sungjoon_sorted:
    total += i
    if total > m:
        break
    else:
        number += 1

print(number)