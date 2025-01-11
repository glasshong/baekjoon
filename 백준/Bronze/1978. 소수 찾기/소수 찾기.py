N = int(input())
l = []
l = list(input().split())
if '1' in l:
    l.remove('1')
a = []
for i in l:
    for j in range(2, int(i)):
        if int(i) % j == 0:
            a.append(i)
            break
print(len(l)-len(a))