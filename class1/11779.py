n = int(input())
m = int(input())
graph = [[] for _ in range(m+1)]

for i in range(m):
    a,b, c= map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

# maybe dijkstra?
INF = 1000000000000000000000

dp = [INF]*(m+1)
dp[start] = 0

dp_cir = [[] for _ in range(m+1)]
visited = [0]*(m+1)
visited[start] = 1

from collections import deque

def dik(s):

    q = deque()
    q.append((s,0))
    min_cir = [s]

    while q:
        cur = q.popleft()
        
        adj_lst = graph[cur[0]]
        visited[cur[0]] = 1

        min_len = 100000
        iter = 0
        index = -1

        for node in adj_lst:
            # 여기를 분리?
            # dp[node[0]] = min(dp[node[0]], cur[1] + node[1])
            if dp[node[0]] > cur[1] + node[1]:
                dp[node[0]] = cur[1] + node[1]
                dp_cir[node[0]]= min_cir
                dp_cir[node[0]].append(node[0])
            else:
                pass

            if min_len > node[1] and visited[node[0]] == 0:
                min_len = node[1]
                index = iter
                        
            iter += 1

        if index == -1:
            break
        min_cir.append(adj_lst[index][0])

        q.append((adj_lst[index][0] , cur[1] + adj_lst[index][1]))



dik(start)

print(dp[end])
print(len(dp_cir[end]))
print(dp_cir[end])