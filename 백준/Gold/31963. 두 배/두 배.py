import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

count = 0
for i in range(n-1):
    while l[i] > l[i+1]:
        l[i+1] *= 2
        count += 1
    
print(count)