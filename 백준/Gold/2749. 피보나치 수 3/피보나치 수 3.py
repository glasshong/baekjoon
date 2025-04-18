import sys
input = sys.stdin.readline

n = int(input()) % (15 * 10**5) # 피사노 주기

dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 1000000

print(dp[n])