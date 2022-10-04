import sys
input = sys.stdin.readline

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(1<<n) for _ in range(n)]

def back_tracking(cur, visited):    
    if dp[cur][visited] != 0:
        return dp[cur][visited]

    if visited == (1<<n) -1 :
        if mat[cur][0]: 
            return mat[cur][0]
        else:
            return 16000000
    
    return_min = 16000000


    for i in range(1,n):
        if not mat[cur][i]:
            continue
        if visited & (1<<i):
            continue
        
        a =  back_tracking(i,visited | (1<<i)) + mat[cur][i]
        if return_min > a:
            return_min = a
        
    dp[cur][visited] = return_min
    
    return return_min


print(back_tracking(0,1))