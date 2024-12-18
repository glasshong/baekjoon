import math
N = int(input())
l = list(map(int, input().split()))
T, P = map(int, input().split())
a = 0
for i in l:
    a += math.ceil(i / T)
print(a)
print(N // P, N % P, sep=' ')