l = []
for _ in range(28):
    l.append(int(input()))

for i in range(1, 31):
    if i not in l:
        print(i)