N = int(input())
l = list(map(int, input().split()))
l.sort()
s = 0
for i in range(N):
    s += l[i] * (N-i)
print(s)