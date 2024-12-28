import sys
import statistics

def my_round(val):
    if abs(val) - abs(int(val)) >= 0.5:
        if val >= 0:
            return int(val) + 1
        else:
            return int(val) - 1
    else:
        return int(val)

N = int(sys.stdin.readline())
l = []
for _ in range(N):
    l.append(int(sys.stdin.readline()))

print(my_round(statistics.mean(l)))
print(statistics.median(l))
m = statistics.multimode(l)
m.sort()
if len(m) >= 2:
    print(m[1])
else:
    print(m[0])
print(max(l)-min(l))