T = 10

def cal(curindex):
    if len(mat[curindex]) == 4:
        cal(int(mat[curindex][2]))
        cal(int(mat[curindex][3]))

        if mat[curindex][1] == '+':
            mat[curindex][1] = int(mat[int(mat[curindex][2])][1]) + int(mat[int(mat[curindex][3])][1])
        elif mat[curindex][1] == '-':
            mat[curindex][1] = int(mat[int(mat[curindex][2])][1]) - int(mat[int(mat[curindex][3])][1])
        elif mat[curindex][1] == '*':
            mat[curindex][1] = int(mat[int(mat[curindex][2])][1]) * int(mat[int(mat[curindex][3])][1])
        elif mat[curindex][1] == '/':
            mat[curindex][1] = int(mat[int(mat[curindex][2])][1]) / int(mat[int(mat[curindex][3])][1])
                        

for tc in range(1, T+1):
    n = int(input())
    mat = [0] + [ input().split() for _ in range(n)]
    cal(1)
    print(f'#{tc} {int(mat[1][1])}')