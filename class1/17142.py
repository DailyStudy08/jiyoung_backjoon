n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

from collections import deque
import copy
import itertools


def bfs(start_array, visited):
    
    q = deque(start_array)

    dx = [1,-1, 0, 0]
    dy = [0,0, 1, -1]

    re_max = 0

    for start in start_array:
        visited[start[0]][start[1]] = 1

    while q:
        cur = q.popleft()

        for d in range(4):
            next = (cur[0] + dx[d], cur[1]+ dy[d])
            if 0 <= next[0] < n and 0<= next[1] < n and visited[next[0]][next[1]] == 0:
                visited[next[0]][next[1]] = visited[cur[0]][cur[1]] +1
                q.append(next)
                
                if re_max < visited[next[0]][next[1]]:
                    re_max = visited[next[0]][next[1]]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                return -1
    
    return re_max -1

can_start = []

flag_2 = True
for i in range(n):
    for j in range(n):
        if mat[i][j] == 0:
            flag_2 = False
            break
    if not flag_2 :
        break




for i in range(n):
    for j in range(n):
        if mat[i][j] == 2:
            can_start.append((i,j))
            mat[i][j] = 0

combi = itertools.combinations(range(len(can_start)), m)

min_answer = 2500


for comb in combi:
    
    start_arr = []
    
    for index in comb:
        start_arr.append(can_start[index])
    
    ans = bfs(start_arr, copy.deepcopy(mat))

    if ans < min_answer and ans != -1:
        min_answer = ans

if min_answer == 2500:
    min_answer = -1

if flag_2 :
    min_answer = 0

print(min_answer)
