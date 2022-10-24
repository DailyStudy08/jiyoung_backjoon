import sys
input = sys.stdin.readline

n = int(input())
mat = [list(map(int, list(input().strip()))) for _ in range(n)]
answer = [0]*((25**2)//2 +100)
di = [1,-1,0,0]
dj = [0,0, 1, -1]

def dfs(cur, mark):
    for d in range(4):
        next = (cur[0]+di[d] , cur[1]+dj[d])
        if 0<= next[0] < n and 0<= next[1] < n  and mat[next[0]][next[1]] == 1:
            mat[next[0]][next[1]] = mark
            dfs(next, mark)


mark_now = 2
for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            mat[i][j] = mark_now
            dfs((i,j) , mark_now)
            mark_now += 1

real_answer = []
for i in range(n):
    for j in range(n):
        if mat[i][j]:
            answer[mat[i][j]] +=1


for i in range((25**2)//2 +100):
    if answer[i] != 0:
        real_answer.append(answer[i])


real_answer.sort()

print(len(real_answer))
for i in range(len(real_answer)):
    print(real_answer[i])

