l = []
for _ in range(10):
    l.append(int(input()))
print(int(sum(l)/10))
print(max(set(l), key=l.count))