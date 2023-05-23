n, m = map(int, input().split())

mem_arr = list(map(int, input().split()))
cost_arr = list(map(int, input().split()))

zip_arr = list(zip(mem_arr, cost_arr))
sorted_zip = sorted(zip_arr, key= lambda x : (x[1], -x[0]))

dp = [[0]*10000 for _ in range(101)]

if sorted_zip[0][1] == 0:
    dp[1][0] = sorted_zip[0][0]

for i in range(1,len(mem_arr) +1):
    for j in range(10000):
        if j < cost_arr[i-1]:
            dp[i][j] =  dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-cost_arr[i-1]] + mem_arr[i-1] , dp[i-1][j] )


min_cost = 10000

for i in range(1,len(mem_arr)+1):
    for j in range(10000):
        if dp[i][j] >= m and min_cost > j:
            min_cost = j

print(min_cost)

