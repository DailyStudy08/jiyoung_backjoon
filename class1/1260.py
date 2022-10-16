from collections import deque
n,m,v = map(int, input().split())

adj_lst = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

for i in range(1,n+1):
    adj_lst[i].sort()


visited = [False]*(n+1)
def dfs(cur):
    print(cur, end =' ')
    for adj in adj_lst[cur]:
        if visited[adj] == False:
            visited[adj] = True
            dfs(adj)

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        cur = q.popleft()
        print(cur, end=' ')

        for adj in adj_lst[cur]:
            if visited[adj] == False:
                visited[adj] = True
                q.append(adj)

visited[v] = True
dfs(v)
visited = [False]*(n+1)
visited[v] = True
print()
bfs(v)

