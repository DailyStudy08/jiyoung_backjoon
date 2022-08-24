dp = [0]* 12
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7
dp[5] = 13
dp[6] = 24
dp[7] = 44
dp[8] = 81
dp[9] = 149
dp[10] = 274
dp[11] = 504

T = int(input())
for i in range(1,T+1):
    n = int(input())
    print(dp[n])
    