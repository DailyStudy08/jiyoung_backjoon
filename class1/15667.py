import sys
# input = sys.stdin.read
# output = sys.stdout.write
f =  open('input.txt', 'r')
input = f.read

n = int(input())
k = 1
while (1+ k + k**2) != n:
    k +=1
print(k)