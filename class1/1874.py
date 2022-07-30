import sys

input = sys.stdin.read
output = sys.stdout.write

def sol():
    n, *wanted_list = map(int,input().split())
    stack = []
    now_input = 1
    s = ''
    not_found = False

    for i in wanted_list:
        now_output = i

        while True:
            if stack and stack[-1] == now_output:  
                stack.pop()
                s += '-\n'
                break
        
            stack.append(now_input)
            s += '+\n'
            now_input +=1

            if now_input > n+1:
                not_found = True
                break
        
        if not_found :
            break

    if not_found:
        return 'NO'
    else :
        return s

output(sol())
    

