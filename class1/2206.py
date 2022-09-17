import sys
from collections import deque
input = sys.stdin.readline

di = [1,-1, 0 , 0]
dj = [0,0, 1, -1]

def bfs(start):
    q = deque([start])
    visited[start[0]][start[1]] = 1

    while q:
        cur = q.popleft()

        if cur == (n-1,m-1):
            answer_lst.append(visited[n-1][m-1])

        for d in range(4):
            next = (cur[0] + di[d] , cur[1] + dj[d])
            if 0<= next[0] <= n-1 and 0<= next[1] <= m-1:
                if visited[next[0]][next[1]] == 0:
                    if mat[next[0]][next[1]]:
                        visited[next[0]][next[1]] = visited[cur[0]][cur[1]] +1
                        new_visited = [[0]*m for _ in range(n)]
                        bfs_break_after(next, new_visited,visited[next[0]][next[1]] )
                    else:
                        visited[next[0]][next[1]] = visited[cur[0]][cur[1]] +1
                        q.append(next)

def bfs_break_after(start, new_visited, start_score):
    q = deque([start])
    new_visited[start[0]][start[1]] = start_score

    while q:
        cur = q.popleft()

        if cur == (n-1,m-1):
            answer_lst.append(new_visited[n-1][m-1])

        for d in range(4):
            next = (cur[0] + di[d] , cur[1] + dj[d])
            if 0<= next[0] <= n-1 and 0<= next[1] <= m-1:
                if new_visited[next[0]][next[1]] == 0 and mat[next[0]][next[1]] == 0:
                    new_visited[next[0]][next[1]] = new_visited[cur[0]][cur[1]] +1
                    q.append(next)






n, m = map(int, input().split())
mat = [list(map(int,list(input().strip()))) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
break_count = 1
answer_lst = []

bfs((0,0))
if answer_lst:
    print(min(answer_lst))
else:
    print(-1)

