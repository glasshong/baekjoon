def new_round(val):
    if val - int(val) >= 0.5: 
        return int(val)+1
    else:
        return int(val)

import sys
n = int(sys.stdin.readline())
l = []
for _ in range(n):
    l.append(int(sys.stdin.readline()))
l.sort()

r = new_round(n * 0.15) 
f = l[0+r:n-r]
if n == 0:
    print(0)
else:
    print(new_round(sum(f)/(len(f))))