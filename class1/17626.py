import sys
input = sys.stdin.readline

dp = [0]*50001

dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 1

for i in range(2,50001):
    cnt = 0
    a = int(i**(1/2))
    dp[i] = 1 + dp[i- a**2]
    for j in range(int(i**(1/2))-1, 0 , -1 ):
        dp[i] = min(dp[i], 1+ dp[i-j**2])

n = int(input())

print(dp[n])


