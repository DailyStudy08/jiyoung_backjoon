import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
adj_lst = [[[] for _ in range(m)] for _ in range(n)]
visited = [[False]*m for _ in range(n)]
cnt = [[0]*m for _ in range(n)]
start = []


for i in range(n):
    for j in range(m):
        if j+1 < m :
            adj_lst[i][j].append((i,j+1))
        if j-1 >=0:
            adj_lst[i][j].append((i,j-1))
        if i-1 >= 0:
            adj_lst[i][j].append((i-1,j))
        if i+1 < n:
            adj_lst[i][j].append((i+1,j))
        
        if mat[i][j] == 1:
            visited[i][j] = True
            start.append((i,j))
        
        if mat[i][j] == -1:
            visited[i][j] = True

def bfs(start):
    q = deque()
    for s in start:
        q.append(s)

    while q:
        v = q.popleft()

        for i in adj_lst[v[0]][v[1]]:
            if not visited[i[0]][i[1]]:
                cnt[i[0]][i[1]] = cnt[v[0]][v[1]] +1
                visited[i[0]][i[1]] = True
                q.append(i)

bfs(start)  
ans = 0
is_not_rooten = False
for i in range(n):
    for j in range(m):
        if ans < cnt[i][j]:
            ans = cnt[i][j]
        
        if cnt[i][j] == 0 and visited[i][j] == False:
            ans = -1
            is_not_rooten = True
            break
    if is_not_rooten:
        break

print(ans)



