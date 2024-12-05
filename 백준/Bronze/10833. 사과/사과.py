N = int(input())
l = 0
for i in range(N):
    a, b = map(int, input().split())
    l += b % a
print(l)