import sys
input = sys.stdin.readline
output = sys.stdout.write
# f =  open('input.txt', 'r')
# input = f.readline


l  = int(input())
s = input().strip()
r = 31
M = 1234567891
sum = 0
cnt = 0
for c in s:
    temp = (ord(c) - ord('a') +1)
    for a in range(cnt):
        temp =  (temp * r) %M 
    sum += temp
    sum = sum%M
    cnt +=1

print(sum)