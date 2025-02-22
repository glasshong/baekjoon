import sys
input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
    l.append(float(input()))
l.sort()
for i in range(7):
    print("{:.3f}".format(l[i]))