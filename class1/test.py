def solution(n, t, m, p):
    answer_str = ''
    dic = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15:'F'}
    for i in range(t*m):
        if i == 0:
            answer_str += '0'
            
        temp_str = ''
        while i!= 0:
            temp_int = i%n
            if temp_int < 10:
                temp_str += str(temp_int)
                i//=n
            else:
                temp_str += dic[temp_int]
                i//=n
        
        temp_str = temp_str[::-1]
        answer_str += temp_str
    answer = ''
    
    cnt = 0
    for i in range(t*m):   # 'answer'   =>  'a' , 'n' , 's', 'w'
        if cnt == t: 
            break
            
        if (i+1)%m == p%m:
            answer += answer_str[i]
            cnt +=1
        
    
    return answer