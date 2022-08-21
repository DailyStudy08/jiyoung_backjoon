import sys
sys.setrecursionlimit(100000)
N, M, R = map(int, sys.stdin.readline().split())
order = [0]*(N+1)  # 방문순서
cnt = 0

# dfs 함수 만들기
def dfs(g, s, visited):
    # 시작노드 방문처리
    visited[s] = True
    global cnt
    cnt += 1
    order[s] = cnt
    for i in g[s]:  # 현재 노드와
        if not visited[i]:   # 연결된 노드가 방문되지 않았을 경우
            dfs(g, i, visited)


visited = [False] * (N+1)

graph = [[] for _ in range(N+1)]
# 그래프 만들기
for i in range(M):      # N줄 반복
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(len(graph)):
    graph[i].sort()

dfs(graph, R, visited)
for i in range(1,N+1):
    print(order[i])