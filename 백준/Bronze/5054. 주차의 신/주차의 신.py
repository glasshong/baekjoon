t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    s = (l[n-1]-l[0])*2
    print(s)