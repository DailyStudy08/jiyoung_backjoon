import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
# parents = [0]*n
adj_lst  = [[] for _ in range(n+1)]
parent_lst = [0]*(n+1)
visited = [False]*(n+1)
def dfs(cur):

    for i in adj_lst[cur]:
        if not visited[i]:
            visited[i] = True
            parent_lst[i] = cur
            dfs(i)

for i in range(n-1):
    a,b = map(int,input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

dfs(1)
for i in range(2,n+1):
    print(parent_lst[i])


