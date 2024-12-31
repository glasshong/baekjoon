import sys
s = set()
for i in range(int(sys.stdin.readline())):
    l = list(sys.stdin.readline().strip().split())
    a = l[0]
    if len(l) == 2:
        x = int(l[1])
    if a == 'add':
        s.add(x)
    elif a == 'remove':
        s.discard(x)
    elif a == 'check':
        if x in s:
            print(1)
        else:
            print(0)     
    elif a == 'toggle':
        if x in s:
            s.discard(x)
        else:
            s.add(x)
    elif a == 'all':
        s = set(range(1, 21))
    else:
        s.clear()