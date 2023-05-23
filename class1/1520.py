## 정답코드

m, n = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 1 , 0 , 0]
dy = [0,0, -1, 1]

dp = [[-1]*n for _ in range(m)]
dp[0][0] = 1


def dfs(cur):
    if cur == (m-1, n-1):
        return 1

    dfs_sum = 0

    for d in range(4):
        next = (cur[0]+dx[d] , cur[1]+ dy[d])
        if 0<= next[0]< m and 0<= next[1]<n and mat[cur[0]][cur[1]] > mat[next[0]][next[1]]:


            ######################################################3
            # 요부분만 수정
            if dp[next[0]][next[1]] != -1:
                dfs_sum += dp[next[0]][next[1]]
            else:
                dfs_sum += dfs(next)
            ######################################################3

    dp[cur[0]][cur[1]] = dfs_sum
    
    return dfs_sum

print(dfs((0,0)))


## 처음 코드


m, n = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 1 , 0 , 0]
dy = [0,0, -1, 1]

dp = [[-1]*n for _ in range(m)]
dp[0][0] = 1


def dfs(cur):
    if cur == (m-1, n-1):
        return 1

    dfs_sum = 0

    for d in range(4):
        next = (cur[0]+dx[d] , cur[1]+ dy[d])
        if 0<= next[0]< m and 0<= next[1]<n and mat[cur[0]][cur[1]] > mat[next[0]][next[1]]:
            dfs_sum += dfs(next)

    dp[cur[0]][cur[1]] = dfs_sum
    
    return dfs_sum

print(dfs((0,0)))
    