A = int(input())
seq = list(map(int, input().split(' ')))
dp = [0]*A

dp[0] = seq[0]

for i in range(A):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j] + seq[i])
        else:
            dp[i] = max(dp[i], seq[i])

print(max(dp))