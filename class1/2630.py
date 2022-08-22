import sys
input = sys.stdin.readline

n = int(input())
mat = [list(map(int,input().split())) for _ in range(n)]

def divide_two(x1,x2,y1,y2,n):
    sum = 0
    for i in range(x1,x2):
        for j in range(y1,y2):
            sum += mat[i][j]
    
    if sum == 0:
        return (1,0)
    elif sum == n*n:
        return (0,1)
    else:
        m = n//2
        white = divide_two(x1,x2-m,y1,y2-m,m)[0]+divide_two(x1+m,x2,y1,y2-m,m)[0]+divide_two(x1,x2-m,y1+m,y2,m)[0]+divide_two(x1+m,x2,y1+m,y2,m)[0]
        blue =  divide_two(x1,x2-m,y1,y2-m,m)[1]+divide_two(x1+m,x2,y1,y2-m,m)[1]+divide_two(x1,x2-m,y1+m,y2,m)[1]+divide_two(x1+m,x2,y1+m,y2,m)[1]
        return (white, blue)

print(divide_two(0,n,0,n,n)[0])
print(divide_two(0,n,0,n,n)[1])
