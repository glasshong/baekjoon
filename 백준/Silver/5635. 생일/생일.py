import datetime
n = int(input())
l = {}
for i in range(n):
    N, D, M, Y = input().split()
    l[N] = datetime.date(int(Y), int(M), int(D))
print(max(l, key=l.get))
print(min(l, key=l.get))