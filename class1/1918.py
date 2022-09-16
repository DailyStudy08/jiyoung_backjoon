s = input().strip()

priority_dic = {'+': 1, '-': 1, '*': 2, '/': 2 , '(':0, ')':-1}
stack = []
new_str = ''
for c in s:
    if c == '+' or c == '-' or c == '*' or c== '/' :
        while stack:
            d = stack.pop()
            if priority_dic[d] >= priority_dic[c]:
                if d != '(' and d != ')':
                    new_str += d
            else:
                stack.append(d)
                break
        stack.append(c)
    elif c == ')':
        while stack:
            d = stack.pop()
            if priority_dic[d] >= priority_dic[c]:
                if d != '(' and d != ')':
                    new_str += d
                if d == '(':
                    break
    elif c == '(':
        stack.append(c)
    else:
        new_str += c

while stack:
    d = stack.pop()
    if d != '(' and d != ')':
        new_str += d

print(new_str)