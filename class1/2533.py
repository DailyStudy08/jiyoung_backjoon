n = int(input())

graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [0]*(n+1)
visited = [0]*(n+1)

def dp_dfs(cur):
    if dp[cur] :
        return dp[cur]

    visited[cur] = 1
    
    to_sum = 0
    child_node = 0

    for node in graph[cur]:
        if visited[node] == 0 :
            to_sum += dp_dfs(node)
            child_node += 1
    
    if child_node == 0:
        return 0

    to_sum += 1
    dp[cur] = to_sum
    return to_sum

visited[1] = 1
print(dp_dfs(1))

