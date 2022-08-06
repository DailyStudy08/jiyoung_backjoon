from re import I
import sys
import math
# input = sys.stdin.read
# output = sys.stdout.write
f =  open('input.txt', 'r')
input = f.readline

def test():
    # n, m , *lst = map(int, input().split())
    n = int(input())
    m = int(input())
    lst = list(map(int,input().split()))
    ful_btn = [0,1,2,3,4,5,6,7,8,9]
    num_btn = [x for x in ful_btn if not x in lst]
    num_btn.sort()
    num_len = len(str(n)) # 자릿수

    lst_n = list(map(int, list(str(n))))

    if not lst:   # 고장 번호 x
        print(min([abs(n-100),num_len]))
    elif not num_btn: # 전부 고장
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
                one_plus_min = one_plus_min*10 + min_num
        else:
            if sec_min:
                one_plus_min = sec_min*(10**num_len)

        # 한 자리 적은거 중 최대
        one_minus_max = 0
        for i in range(num_len -1):
            one_minus_max = one_minus_max*10 + max_num

        if num_len == 1:
            one_minus_max = -100
        

        equal_max = 0
        equal_min = 0

        lst_prop_n = []
        break_bool = False

        for a in lst_n:
            if a in num_btn:
                lst_prop_n.append(a)
            else :
                lst_prop_n.append(a)
                break_bool = True
                break
            

        min_index = -1
        max_index = -1
        min_a = 0
        max_a = 0

        for i in range(len(lst_prop_n)):
            if lst_prop_n[i] < num_btn[-1]:
                min_index = i
                min_a = lst_prop_n[i]
            if lst_prop_n[i] > num_btn[0]:
                max_index = i
                max_a = lst_prop_n[i]
        
        if min_index == -1:
            equal_min = - 100
        else:
            for i in num_btn:
                if min_a < i:
                    min_a = i
                    break

            for i in range(min_index):
                equal_min = equal_min*10 + lst_n[i]
            
            equal_min = equal_min*10 + min_a
            for j in range(num_len- min_index-1):
                equal_min = equal_min*10 + num_btn[0]
        
        if max_index == -1:
            equal_max = -100
        else:
            for i in range(len(num_btn)):
                if max_a > num_btn[len(num_btn)-1-i] :
                    max_a = num_btn[len(num_btn)-1-i]
                    break

            for i in range(max_index):
                equal_max = equal_max*10 + lst_n[i]
            
            equal_max = equal_max*10 + max_a
            for j in range(num_len- max_index-1):
                equal_max = equal_max*10 + num_btn[-1]

        if not break_bool:
            equal_max = n
            equal_min = n
        
        ans_lst = [abs(100-n), abs(equal_min - n)+num_len , abs(equal_max - n)+ num_len , abs(one_minus_max - n)+ num_len-1 , abs(one_plus_min-n)+ num_len+1]

        print(min(ans_lst))


k = 31
for i in range(k):
    test()