N = int(input())

f = 1
for i in range(2, N+1):
    f *= i

t = 0
f = str(f)
for j in range(1, len(f)+1):
    if int(f[-j]) == 0:
        t += 1
    else:
        break   
print(t)