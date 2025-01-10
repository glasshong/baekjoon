import sys
input = sys.stdin.readline

N = int(input())
l = []
for _ in range(N):
    l.append(input().strip())
l = list(set(l))

l.sort()
l.sort(key=len)

for i in l:
	print(i)