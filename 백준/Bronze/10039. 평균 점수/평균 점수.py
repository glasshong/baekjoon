t = 0
for i in range(5):
    p = int(input())
    if p < 40:
        p = 40
    t += p
print(int(t/5))