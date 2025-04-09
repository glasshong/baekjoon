import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
l = list(map(int, input().split()))
l.sort()

d = []
for i in range(1, n):
    d.append(l[i]-l[i-1])
d.sort()

answer = d[:n-k]
print(sum(answer))