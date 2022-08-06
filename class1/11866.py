import sys
input = sys.stdin.read
output = sys.stdout.write
# f =  open('input.txt', 'r')
# input = f.read

n, k = map(int, input().split())

ans_lst = []

num_lst = list(range(1,n+1))
index = 0

while num_lst :
    index = (index + k -1)% len(num_lst)

    ans_lst.append(num_lst.pop(index))

s = '<'
for i in ans_lst:
    s += str(i)+', '

s= s.strip(' ,')
s+= '>'

print(s)