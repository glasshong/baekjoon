import statistics
l = []
for _ in range(10):
    l.append(int(input()))
print(statistics.mean(l))
print(statistics.mode(l))