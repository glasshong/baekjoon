import sys
from collections import Counter
N = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in range(N)]
l.sort()

print(round(sum(l)/N))
print(l[N//2])
new_l = sorted(Counter(l).items(), key = lambda x : (-x[1], x[0]))
if N == 1:
    print(l[0])
else:
    if new_l[0][1] != new_l[1][1]:
        print(new_l[0][0])
    else:
        print(new_l[1][0])
print(max(l)-min(l))