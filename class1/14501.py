n = int(input())

plan = []


for i in range(n):
    plan.append(list(map(int, input().split())))

maxFee = 0

dp = [0]* (n+1)

if plan[n-1][0] <= 1:
    dp[n-1] = plan[n-1][1]

for i in range(n-2, -1, -1):
    
    if plan[i][0] + i <= n:
        dp[i] = max(dp[i+1], plan[i][1] + dp[i+ plan[i][0]])
    else:
        dp[i] = dp[i+1]

print(dp[0])