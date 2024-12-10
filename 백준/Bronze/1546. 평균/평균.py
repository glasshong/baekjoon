N = int(input())
l = list(map(int, input().split()))
a = 0
for i in range(N):
    a += l[i]/max(l)*100
print(a/N) 