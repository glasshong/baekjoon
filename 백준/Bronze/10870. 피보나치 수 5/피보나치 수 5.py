l = [0, 1]
for i in range(1, 21):
    l.append(l[i]+l[i-1])
n = int(input())
print(l[n])