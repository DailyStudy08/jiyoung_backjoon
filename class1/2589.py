from collections import deque

h, w = map(int, input().split())

mat = [0]*h

for i in range(h):
    mat[i] = input().strip()

answer = 0

def bfs(start):
    q = deque()
    q.append(start)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[0]*w for _ in range(h)]
    visited[start[0]][start[1]] = 1
    max_len = 0

    while q:
        cur = q.popleft()
        if max_len < cur[2]:
            max_len = cur[2]

        for d in range(4):
            next = (cur[0]+ dx[d], cur[1] + dy[d], cur[2]+1)
            if 0 <= next[0] <= h-1 and 0<= next[1] <= w-1:
                if visited[next[0]][next[1]] == 0 and mat[next[0]][next[1]] == 'L':
                    visited[next[0]][next[1]] = 1
                    q.append(next)

    return max_len


for i in range(h):
    for j in range(w):
        tmp_len = 0
        if mat[i][j] == 'L':
            tmp_len = bfs((i,j,0))

        if answer < tmp_len:
            answer = tmp_len

print(answer)