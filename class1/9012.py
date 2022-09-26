T = int(input())

for tc in range(1,T+1):
    stack = []
    parenthesis_lst = input().strip()
    flag = True

    for i in range(len(parenthesis_lst)):
        if parenthesis_lst[i] == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                flag = False
                break
    
    if flag and not stack:
        print('YES')
    else:
        print('NO')