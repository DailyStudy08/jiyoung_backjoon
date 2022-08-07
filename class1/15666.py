import sys
input = sys.stdin.read
output = sys.stdout.write
# f =  open('input.txt', 'r')
# input = f.read
n, m , *lst = map(int, input().split())
lst = list(set(lst))
lst.sort()
tmp_lst = []

def dfs(level,a, a_lst):
    if level == m:
        s= ''
        for i in a_lst:
            s +=  str(i)+' '
        print(s)
        return
    
    for i in range(a,len(lst)):
        a_lst.append(lst[i])
        dfs(level+1,i, a_lst)
        a_lst.pop()

dfs(0,0,tmp_lst)