import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

adj_lst = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

visited = [False]*(n+1)
def bfs(start):
    q = [start]
    cnt = -1
    visited[start] = True
    while q:
        cnt += 1
        v = q.pop()
        for i in adj_lst[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

    return cnt

print(bfs(1))