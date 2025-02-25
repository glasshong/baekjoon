N = int(input())
l = [0] * N

l[0] = 3
for i in range(1, N):
    l[i] = l[i-1] + (i+1) * (i+2) + ((i+1) * (i+2)) // 2

print(l[N-1])