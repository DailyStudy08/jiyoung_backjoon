import sys
input = sys.stdin.readline

def node_delete(x):
    global visited, graph
    visited[x] = -1
    for i in graph[x]:
        visited[i] = -1

def dfs(root):
    global visited, graph, cnt
    if graph[root] == [] or graph[root] == [x]:
        cnt += 1
        return
    for j in graph[root]:
        if not visited[j]:
            dfs(j)


# 노드의 갯수
V = int(input())
# 노드마다 1씩 더해준 것
parents = list(map(int, input().split()))
# 지울 노드
graph = [[] for _ in range(V)]
start = 0
for idx in range(V):
    if parents[idx] == -1:
        start = idx
    else:
        graph[parents[idx]].append(idx)
# print(graph)
x = int(input())
visited = [0]*(V)
cnt = 0

node_delete(x)
dfs(start)

if V == 1:
    cnt = 0
print(cnt)
