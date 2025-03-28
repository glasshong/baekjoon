import sys
input = sys.stdin.readline

from collections import Counter

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
l = []

cnt = Counter(a)
for i in b:
    if i in cnt:
        l.append(cnt[i])
    else:
        l.append(0)

print(*l)