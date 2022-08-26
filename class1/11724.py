import sys
input = sys.stdin.readline

n, m = map(int, input().split())
def dfs(v):
    visited[v] = True
    for i in adj_lst[v]:
        if not visited[i]:
            dfs(i)



visited = [False]*(n+1)
visited[0] = True

adj_lst = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

cnt = 0

for i in range(n+1):
    if visited[i]:
        pass
    else:
        dfs(i)
        cnt += 1


print(cnt)

