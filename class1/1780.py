import sys
input = sys.stdin.readline

exp_n = int(input())
mat = [list(map(int, input().split())) for _ in range(exp_n)]
m = 0

for i in range(8):
    if 3**i == exp_n:
        m = i
        break


answer_lst = [0,0,0]

def divide_mat(row, col , n):

    index = mat[row][col]

    for i in range(int(3**n)):
        for j in range(int(3**n)):
            if index == mat[row+i][col+j]:
                pass
            else:
                index = 4
                break
        
        if index ==4:
            break

    if index == -1:
        answer_lst[0] += 1
    elif index == 1:
        answer_lst[2] +=1 
    elif index == 0:
        answer_lst[1] += 1
    else:
        for i in range(9):
            a = i//3
            b = i%3
            divide_mat(row+int(3**(n-1)*a), col+int(3**(n-1)*b) , n-1)
    
divide_mat(0,0,m)
print(answer_lst[0])
print(answer_lst[1])
print(answer_lst[2])