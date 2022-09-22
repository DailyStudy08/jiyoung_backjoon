import sys

sys.setrecursionlimit(500000)
n = int(input())

mat = [[1,1], [1,0]]

def power(n):
    if n == 1:
        return mat

    if n%2 == 0:
        tmp_mat = power(n//2)
        return_mat = [[0,0], [0,0]]
        for i in range(2):
            for j in range(2):
                return_mat[i][j] = (tmp_mat[i][0]*tmp_mat[0][j] + tmp_mat[i][1]*tmp_mat[1][j])%1000000007 

        return return_mat
    else:
        tmp_mat = power((n-1)//2)
        return_mat_1 = [[0,0], [0,0]]
        for i in range(2):
            for j in range(2):
                return_mat_1[i][j] = (tmp_mat[i][0]*tmp_mat[0][j] + tmp_mat[i][1]*tmp_mat[1][j])%1000000007
        

        return [[return_mat_1[0][0] + return_mat_1[1][0] , return_mat_1[1][0]+ return_mat_1[1][1]], [return_mat_1[0][0], return_mat_1[0][1]]]


if n == 1:
    print(1)
else:
    print(power(n-1)[0][0]%1000000007)