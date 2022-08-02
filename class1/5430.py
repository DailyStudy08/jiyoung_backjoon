import sys

input = sys.stdin.readline

# f =  open('input.txt', 'r')
# input = f.readline

T = int(input())

for i in range(T):
    func_line = input().strip()
    n = int(input())
    temp_lst = input().strip().strip('[]').split(',')  ## list 전처리가 뭔가 더 깔끔한게 있을거 같은데 귀찮게 됐네..
    if temp_lst == ['']:
        lst = []
    else :
        lst = list(map(int,temp_lst))
    rev = False
    post_index = 0
    rear_index = 0
    total = 0
    for c in func_line:
        if c == 'R':
            rev = not rev
        
        if c == 'D':
            if rev:
                rear_index += 1
                total += 1
            else :
                post_index += 1
                total +=1
            
            if total > n:
                print('error')
                break
    
    if total > n:
        continue
    
    ans = lst[post_index:n-rear_index]
    if rev:
        ans.reverse()
    
    s =''
    s += '['
    for a in ans:
        s += str(a)+','
    
    s = s.rstrip(',')
    s += ']'
    print(s)

    # print(ans) .... 출력을 list 그대로 하니까 공백 들어가서 틀림.. 출력 이슈로 한시간 반 날린게 레전드



    ## 대략 여기까지 sum(len(func_lines)) .. 70만 * c 번의 계산



        