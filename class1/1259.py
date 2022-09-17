import sys
input = sys.stdin.readline

while True:
    s = list(input().strip())
    a = s[::-1]
    if s == ['0']:
        break
    if s == a:
        print('yes')
    else:
        print('no')