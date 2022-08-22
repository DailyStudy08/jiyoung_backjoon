import sys
# input = sys.stdin.readline
sys.setrecursionlimit(100000)
f = open('input.txt', 'r')
input = f.readline

T = int(input())


def dfs(cur):
    if mat[cur[0]][cur[1]] == 0 or mat[cur[0]][cur[1]] == 2:
        return
    
    if mat[cur[0]][cur[1]] == 1:
        mat[cur[0]][cur[1]] += 1
        visited[cur[0]][cur[1]] = True

    for i in adj_lst[cur[0]][cur[1]]:
        if visited[i[0]][i[1]] == False:
            dfs(i)


for l in range(T):

    m,n,k = map(int,input().split())
    mat = [[0]*m for _ in range(n)]
    for j in range(k):
        a,b = map(int,input().split())
        mat[b][a] = 1
    
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    cnt = 0
    visited = [[False]*m for _ in range(n)]
    adj_lst = [[[] for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for d in range(4):
                col = i + di[d]
                row = j + dj[d]
                if 0<= col < n and 0<= row < m:
                    tmp_tuple = (col, row)
                    adj_lst[i][j].append(tmp_tuple)            

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                cnt += 1
                dfs((i,j))
    print(cnt)
