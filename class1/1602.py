import sys
input = sys.stdin.readline
n,m,q = map(int, input().split())
dog_waiting = [0] + list(map(int, input().split()))
dog_index = [i for i in range(1,n+1)]

INF = 1e9
graph_dist = [[INF]*(n+1) for _ in range(n+1)]
graph_cost = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i== j:
            graph_dist[i][j] = 0
            graph_cost[i][j] = dog_waiting[i]

for i in range(m):
    a,b,c = map(int, input().split())
    if graph_dist[a][b] == 1e9:
        graph_dist[a][b] = c
        graph_dist[b][a] = c
        graph_cost[a][b] = c + max(dog_waiting[a], dog_waiting[b])
        graph_cost[b][a] = c + max(dog_waiting[a], dog_waiting[b])

dog_index = sorted(dog_index, key=lambda x: dog_waiting[x])


for idx in range(1,n+1):
    i = dog_index[idx-1]
    for j in range(1,n+1):
        for k in range(1,n+1):
            if graph_dist[j][k] > graph_dist[j][i] + graph_dist[i][k]:
                graph_dist[j][k] = graph_dist[j][i] + graph_dist[i][k]
            
            if graph_cost[j][k] > graph_dist[j][k] + max(dog_waiting[i], dog_waiting[j], dog_waiting[k]):
                graph_cost[j][k]  = graph_dist[j][k] + max(dog_waiting[i], dog_waiting[j], dog_waiting[k])

           

for a in range(q):
    r,c = map(int, input().split())
    if graph_cost[r][c] == 1e9:
        print(-1)
    else:
        print(graph_cost[r][c])