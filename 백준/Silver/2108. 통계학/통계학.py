import sys
import statistics

N = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in range(N)]

print(round(statistics.mean(l)))
print(statistics.median(l))
m = statistics.multimode(l)
m.sort()
if len(m) >= 2:
    print(m[1])
else:
    print(m[0])
print(max(l)-min(l))