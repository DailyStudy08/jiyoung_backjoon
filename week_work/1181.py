import sys
input = sys.stdin.read
output = sys.stdout.write
# f =  open('input.txt', 'r')
# input = f.read

n, *str_lst = input().split()
str_lst = list(set(str_lst))
n = int(n)
str_lst = sorted(str_lst, key= lambda x: (len(x),x)) 
for s in str_lst:
    print(s)