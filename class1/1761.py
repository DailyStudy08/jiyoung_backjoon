import sys
input = sys.stdin.readline
sys.setrecursionlimit(40000)

n = int(input())
adj_lst = [[] for _ in range(n+1)]

for i in range(n-1):
    
    a,b,c = map(int , input().split())
    adj_lst[a].append((b,c))
    adj_lst[b].append((a,c))

visited = [0]*(n+1)
depth_lst = [0]*(n+1)
parent = [0]*(n+1)
root_to_node = [0]*(n+1)

def dfs(cur, depth):
    for adj in adj_lst[cur]:
        if not visited[adj[0]]:
            parent[adj[0]] = cur
            depth_lst[adj[0]] = depth +1
            visited[adj[0]] = 1
            root_to_node[adj[0]] = root_to_node[cur] + adj[1]
            dfs(adj[0], depth +1)

def cal_lca(a,b):
    if depth_lst[a] > depth_lst[b]:
        while depth_lst[a] != depth_lst[b]:
            a = parent[a]
    else:
        while depth_lst[a] != depth_lst[b]:
            b = parent[b]
    
    while a != b:
        a = parent[a]
        b = parent[b]
    
    return a

dfs(1,0)

m = int(input())

for i in range(m):
    x,y = map(int, input().split())
    c = cal_lca(x,y)
    print(root_to_node[x] + root_to_node[y] -2*root_to_node[c])



