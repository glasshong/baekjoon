N = int(input())
A = list(map(int, input().split()))

revA = A[::-1]

inc = [1]*N
dec = [1]*N

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            inc[i] = max(inc[i], inc[j]+1)
        if revA[j] < revA[i]:
            dec[i] = max(dec[i], dec[j]+1)

dec = dec[::-1]

result = []
for i in range(N):
    result.append(dec[i]+inc[i]-1)

print(max(result))