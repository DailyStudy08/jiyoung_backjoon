import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = 1e9
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i== j:
            graph[i][j] = 0

for i in range(m):
    a,b = map(int, input().split())
    if graph[a][b] == 1e9:
        graph[a][b] = 1
        graph[b][a] = 1


for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[j][k] = min(graph[j][k] , graph[j][i] + graph[i][k])


cabin_sum = 1e9
answer = 0

for i in range(1, n+1):
    tmp_sum = 0
    for j in range(1,n+1):
        tmp_sum += graph[i][j]
    
    if tmp_sum < cabin_sum:
        cabin_sum = tmp_sum
        answer = i

print(answer)
