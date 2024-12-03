d = int(input())
n = list(map(int, input().split()))
a = 0
for i in range(5):
    if n[i] == d:
        a += 1
print(a)