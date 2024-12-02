N = int(input())
l = []
for _ in range(N):
    n = int(input())
    l.append(n)
if l.count(1) > l.count(0):
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')