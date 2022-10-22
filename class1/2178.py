import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

mat = [list(map(int,list(input().strip()))) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def bfs():
    start = (0,0)

    q = deque()
    q.append(start)
    di = [1,-1, 0,0]
    dj = [0,0, 1,-1]
    visited[start[0]][start[1]] = 1
    while q:
        cur = q.popleft()
        
        for d in range(4):
            next =(cur[0]+ di[d] , cur[1]+ dj[d])

            if 0<= next[0] < n and 0<= next[1] < m and visited[next[0]][next[1]] == 0 and mat[next[0]][next[1]] == 1:
                visited[next[0]][next[1]] = visited[cur[0]][cur[1]] +1
                q.append(next)

bfs()

print(visited[n-1][m-1])