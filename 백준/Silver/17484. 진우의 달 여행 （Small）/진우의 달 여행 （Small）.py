import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * m for _ in range(n)] for _ in range(3)]
answer = sys.maxsize

for i in range(3):
    for j in range(m):
        dp[i][0][j] = lst[0][j]

for i in range(1, n):
    for j in range(m):
        if j == 0:
            dp[0][i][j] = dp[1][i-1][j]
            dp[1][i][j] = dp[0][i-1][j+1]
            dp[2][i][j] = min(dp[0][i-1][j+1], dp[1][i-1][j])
        elif j == m-1:
            dp[0][i][j] = min(dp[1][i-1][j], dp[2][i-1][j-1])
            dp[1][i][j] = dp[2][i-1][j-1]
            dp[2][i][j] = dp[1][i-1][j]
        else:
            dp[0][i][j] = min(dp[1][i-1][j], dp[2][i-1][j-1])
            dp[1][i][j] = min(dp[0][i-1][j+1], dp[2][i-1][j-1])
            dp[2][i][j] = min(dp[0][i-1][j+1], dp[1][i-1][j])

        for k in range(3):
            dp[k][i][j] += lst[i][j]

for i in range(3):
    answer = min(answer, min(dp[i][-1]))

print(answer)