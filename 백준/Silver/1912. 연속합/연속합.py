n = int(input())
seq = list(map(int, input().split()))

dp = [0]*n
dp[0] = seq[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + seq[i], seq[i])

print(max(dp)) 