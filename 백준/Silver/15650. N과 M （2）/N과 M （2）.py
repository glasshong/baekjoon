import sys
import itertools
input = sys.stdin.readline

N, M = map(int, input().split())
l = list(range(1, N+1))
c = itertools.combinations(l, M)
a = list(c)

for i in a:
    print(*i)