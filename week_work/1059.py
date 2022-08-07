import sys
input = sys.stdin.read
output = sys.stdout.write
# f =  open('input.txt', 'r')
# input = f.read
l, *lst, n = map(int,input().split())
n_before = 0
n_next = 0
lst.sort()
for i in lst:
    if i > n:
        n_next =i
        break
    else:
        n_before = i

k = (n_next-n -1)+(n-n_before-1)*(n_next-n)
if k < 0:
    k= 0
print(k)