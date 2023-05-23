n = int(input())

can_set = [0]*1000

for i in range(1000):
    if i < 123:
        can_set[i] = 1

    if i//100 == i%10 or (i//10)%10 == i%10 or (i//100) == (i//10)%10:
        can_set[i] = 1
    
    if i//100 == 0 or (i//10)%10 ==0 or i%10 == 0:
        can_set[i] = 1


for i in range(123,1000):
    if can_set[i] == 0:
        print(i)


for i in range(n):
    num, stk , ball = map(int, input().split())

    for j in range(123, 1000):
        tmp_stk = 0
        tmp_ball = 0

        if can_set[j] == 0:
            if j%10 == num%10:
                tmp_stk += 1
            
            if (j//10)%10 == (num//10)%10:
                tmp_stk += 1
            
            if (j//100) == (num//100):
                tmp_stk += 1
            
            if (j//10)%10 == (num//100) or (j//10)%10 == num%10:
                tmp_ball += 1
            
            if j%10 == (num//100) or j%10 == (num//10)%10:
                tmp_ball += 1
            
            if(j//100) == num%10 or (j//100) == (num//10)%10:
                tmp_ball += 1

            if tmp_ball == ball and tmp_stk == stk:
                pass
            else:
                can_set[j] = 1

answer_cnt = 0

for i in range(123,1000):
    if can_set[i] == 0:
        answer_cnt += 1
        print(i)


print(answer_cnt)
