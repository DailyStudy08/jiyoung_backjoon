n = int(input())
dp = [[2**32]*n for _ in range(n+1)]
row_col_lst = []

for i in range(n):
    a,b = map(int, input().split())
    row_col_lst.append((a,b))

for i in range(n):
    dp[i][i] = 0

for i in range(1,n):
    for j in range(0, n-i):
        if i == 1:
            dp[j][j+i] = row_col_lst[j][0]*row_col_lst[j+1][0]*row_col_lst[j+1][1]
            continue

        for k in range(j, j+i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + row_col_lst[j][0] * row_col_lst[k][1] * row_col_lst[j+i][1])


print(dp[0][n-1])
        

        
            


