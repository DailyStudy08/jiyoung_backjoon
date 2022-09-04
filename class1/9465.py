import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    n = int(input())
    mat = [list(map(int,input().split())) for _ in range(2)]

    if n!= 1:
        mat[0][1]  = mat[1][0] + mat[0][1] 
        mat[1][1] = mat[0][0] + mat[1][1]

    for i in range(2,n):
        mat[0][i] = max(mat[1][i-1] + mat[0][i] , mat[1][i-2] + mat[0][i])
        mat[1][i] = max(mat[0][i-1]+ mat[1][i], mat[0][i-2] + mat[1][i])


    print(max(mat[0][n-1], mat[1][n-1])) 