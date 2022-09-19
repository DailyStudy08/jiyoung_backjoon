T = int(input())
code_dic  = {'0001101': 0 , '0011001':1, '0010011':2, '0111101':3 , '0100011':4, '0110001':5, '0101111':6 , '0111011':7 , '0110111':8, '0001011':9  } 

for tc in range(1,T+1):
    n, m = map(int, input().split())
    s = ''
    index = 0
    for i in range(n):
        tmp_str = input().strip()
        if int(tmp_str) != 0:
            for j in range(len(tmp_str)):
                if tmp_str[j] == '1':
                    index = j
                s = tmp_str
        else:
            continue

    start = index-55
    sum_num = 0
    ans =0
    for i in range(8):
        if i%2 == 0:
            sum_num += code_dic[s[start+7*i: start+7*(i+1)]] *3
            ans += code_dic[s[start+7*i: start+7*(i+1)]]
        else:
            sum_num += code_dic[s[start+7*i: start+7*(i+1)]]
            ans += code_dic[s[start+7*i: start+7*(i+1)]]
    

    if sum_num%10 == 0:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} {0}')

    
