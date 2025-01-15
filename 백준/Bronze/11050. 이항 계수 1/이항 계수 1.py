import itertools
N, K = map(int, input().split())
l = list(range(1, N+1))
a = list(itertools.combinations(l, K))
print(len(a))