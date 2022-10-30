import sys
input = sys.stdin.readline

n = int(input())

mat = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            mat[i][j] = max(mat[i][j] , mat[i][k]*mat[k][j])

for i in range(n):
    for j in range(n):
        for k in range(n):
            mat[i][j] = max(mat[i][j] , mat[i][k]*mat[k][j])


for i in range(n):
    print(*mat[i])