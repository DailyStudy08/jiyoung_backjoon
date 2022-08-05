from re import I
import sys
import math
# input = sys.stdin.read
# output = sys.stdout.write
f =  open('input.txt', 'r')
input = f.read

n, m , *lst = map(int, input().split())
ful_btn = [0,1,2,3,4,5,6,7,8,9]
num_btn = [x for x in ful_btn if not x in lst]
num_btn.sort()
num_len = len(str(n)) # 자릿수

lst_n = []
l = n
while l != 0:
    lst_n.append(l%10)
    l = l//10

lst_n.reverse()


if not lst:   # 고장 번호 x
    print(num_len)
if not num_btn: # 전부 고장
    print(abs(n-100))
else:
    min_num = num_btn[0]
    sec_min =0
    if len(num_btn) != 1:
        sec_min = num_btn[1]
    max_num = num_btn[-1]

    # 한 자리 많은거 중 최소
    one_plus_min = 0
    if min_num != 0:
        for i in range(num_len+1):
            one_plus_min += one_plus_min*10 + min_num
    else:
        if sec_min:
            one_plus_min = sec_min*(10**num_len)
    # 한 자리 적은거 중 최대
    one_minus_max = 0
    for i in range(num_len -1):
        one_minus_max = one_minus_max*10 + max_num

    if num_len == 1:
        one_minus_max = -1
    

    equal_max = 0
    equal_min = 0

    lst_index = []
    break_bool = False

    for a in lst_n:
        for idx, i in enumerate(num_btn):
            if a== i:
                lst_index.append(idx)
            else :
                lst_index.append(idx)
                break_bool = True
                break
        if break_bool:
            break
    
    min_index = -1
    max_index = -1

    for i in range(len(lst_index)):
        k = lst_index[i]
        if k != 0:
            min_index = i
        elif k != len(num_btn)-1:
            max_index = i
    
    if min_index == -1:
        pass
    else:
        for i in range(min_index):
            equal_min = equal_min*10 + lst_n[i]
        
        equal_min = equal_min*10 + num_btn[lst_index[min_index]-1]
        for j in range(num_len- min_index-1):
            equal_min = equal_min*10 + num_btn[0]
    
    if max_index == -1:
        pass
    else:
        for i in range(max_index):
            equal_min = equal_min*10 + lst_n[i]
        
        equal_min = equal_min*10 + num_btn[lst_index[max_index]+1]
        for j in range(num_len- max_index-1):
            equal_min = equal_min*10 + num_btn[-1]
    
    ans_lst = [abs(100-n), abs(equal_min - n)+num_len , abs(equal_max - n)+ num_len , abs(one_minus_max - n)+ num_len-1 , abs(one_plus_min-n)+ num_len+1]

    print(min(ans_lst))


