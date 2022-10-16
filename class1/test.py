record =["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]


def solution(record):
    dic = {}
    result_lst = []
    answer = []
    for rec in record:
        query = rec.split()
        if query[0] == 'Enter':
            result_lst.append(('님이 들어왔습니다.', query[1]))
            dic[query[1]] = query[2]
        elif query[0] == 'Leave':
            result_lst.append(('님이 나갔습니다.', query[1]))
        else:
            dic[query[1]] = query[2]
    
    for result in result_lst:
        answer.append(dic[result[1]] + result[0])
    
    return answer

print(solution(record))