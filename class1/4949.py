import sys
input = sys.stdin.readline

while True:
    input_str = input()
    if input_str == '.\n':
        break

    stack = []
    flag = True

    for c in input_str:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')' :
            if stack:
                if stack.pop() == '(':
                    pass
                else:
                    print('no')
                    flag = False
                    break
            else:
                print('no')
                flag = False
                break
        elif c == ']':
            if stack:
                if stack.pop() == '[':
                    pass
                else:
                    print('no')
                    flag = False
                    break
            else:
                print('no')
                flag = False
                break
    else:
        if stack:
            print('no')
            flag = False
            
    if flag: 
        print('yes')