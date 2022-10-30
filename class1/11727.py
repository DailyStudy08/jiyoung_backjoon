import sys
input = sys.stdin.readline


dp = [0]*1001

dp[1] = 1
dp[2] = 3
dp[3] = 5

for i in range(4,1001):
    dp[i] = (2*dp[i-2] + dp[i-1])%10007 


n = int(input())

print(dp[n])