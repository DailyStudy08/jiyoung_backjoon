import sys
input = sys.stdin.readline
# f = open('input.txt', 'r')
# input = f.readline

n = int(input())
mat = []
for i in range(n):
    mat.extend(list(map(int,list(input().strip()))))

def rec(n,lst):
    k = sum(lst)

    if k== 0:
        return '0'
    elif k== n**2:
        return '1'
    else :
        lst1 = []
        lst2 = []
        lst3 = []
        lst4 = []
        for i in range(n//2):
            lst1.extend(lst[i*n:i*n+n//2])
            lst2.extend(lst[i*n+n//2:(i+1)*n])
            lst3.extend(lst[(n//2)*n + i*n:(n//2)*n + i*n + n//2 ])
            lst4.extend(lst[(n//2)*n+i*n+n//2:(n//2)*n+(i+1)*n])
        m = n//2
        return f'({rec(m,lst1)}{rec(m,lst2)}{rec(m,lst3)}{rec(m,lst4)})'


print(rec(n,mat))