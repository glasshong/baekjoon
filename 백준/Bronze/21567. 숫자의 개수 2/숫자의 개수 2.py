a = int(input())
b = int(input())
c = int(input())

idx = [0] * 10
for i in str(a * b * c):
    idx[int(i)] += 1

for i in idx:
    print(i)