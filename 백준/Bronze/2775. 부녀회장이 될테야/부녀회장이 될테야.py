import sys
input = sys.stdin.readline

T = int(input())

dp = [[0]*14 for _ in range(15)]
dp[0] = list(range(1, 15))

for i in range(14):
    for j in range(14):
        dp[i+1][j] = sum([dp[i][k] for k in range(j+1)])

for _ in range(T):
    k = int(input())
    n = int(input())
    print(dp[k][n-1])