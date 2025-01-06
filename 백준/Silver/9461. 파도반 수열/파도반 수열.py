import sys
input = sys.stdin.readline

N = int(input().strip())
l = [1] * 101
l[3] = 2
l[4] = 2
for i in range(5, 101):
    l[i] = l[i-1] + l[i-5]

for i in range(N):
    a = int(input().strip())
    print(l[a-1])