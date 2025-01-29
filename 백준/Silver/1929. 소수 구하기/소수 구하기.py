import sys
input = sys.stdin.readline

M, N = map(int, input().split())

p = [True] * (N+1)

p[0], p[1] = False, False 
for i in range(2, N+1):
    if p[i]: 
        for j in range(i*2, N+1, i): 
            p[j] = False

l = []
for i in range(M, N+1):
    if p[i] == True:
        l.append(i)

for i in l:
    print(i, sep = '\n')