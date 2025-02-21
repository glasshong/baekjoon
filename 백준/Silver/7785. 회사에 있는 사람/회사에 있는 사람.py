import sys
input = sys.stdin.readline

n = int(input())
l = set()

for _ in range(n):
    a, b = map(str, input().split())

    if b == 'enter':
        l.add(a)
    else:
        l.remove(a)

l = list(l)
l.sort(reverse=True)

for i in l:
    print(i)