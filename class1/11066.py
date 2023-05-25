tc = int(input())

for test in range(tc):
    n = int(input())
    size_list  = list(map(int, input().split()))
    
    toSum = {-1:0}

    dp = [[99999999999999999999]*n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 0

    for i in range(n):
        toSum[i] = toSum[i-1] + size_list[i]
    
    for i in range(1,n):
        for j in range(n):
            
            end = j + i

            if end > n-1:
                continue
            
            for cut in range(j, end):
                dp[j][end] = min(dp[j][cut] + dp[cut+1][end] + toSum[end] - toSum[j-1], dp[j][end])
        
    # print(toSum)    

    # print(dp)
    print(dp[0][n-1])
            



    
    

    
    
