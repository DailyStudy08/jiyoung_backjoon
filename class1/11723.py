import sys
input = sys.stdin.readline

n = int(input())

s = 0b00000000000000000000

for i in range(n):
    cmd = input().split()

    if cmd[0] == 'add':
        s =  s | 1<<int(cmd[1])
    elif cmd[0] == 'remove':
        if s& 1<<int(cmd[1]):
            s =  s ^ 1<<int(cmd[1])
    elif cmd[0] == 'check':
        if s& 1<<int(cmd[1]):
            print(1)
        else:
            print(0)
    elif cmd[0] == 'toggle':
        if s& 1<<int(cmd[1]):
            s =  s ^ 1<<int(cmd[1])
        else:
            s =  s | 1<<int(cmd[1])
    elif cmd[0] == 'all':
        s = 0b111111111111111111110
    else :
        s = 0b000000000000000000000
    