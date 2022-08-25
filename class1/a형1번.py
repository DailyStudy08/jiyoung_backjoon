T = int(input())

def fill_place(teca,lst):
    d_sum = 60* 20

    for i in range(8):
        tmp_sum = 0
        visited = [False]*(n+1)
        visited[0] = True
        for k in range(3):
            if i & 1<<k:
                tmp_sum += fill_place_right(teca[k], lst, visited)
            else:
                tmp_sum += fill_place_left(teca[k], lst, visited)

        if tmp_sum < d_sum:
            d_sum = tmp_sum

    return d_sum


def fill_place_left(k,lst, visited):
    index = 0
    d_sum = 0
    p = lst[2*k-1]
    while p != 0:
        if lst[2*k-2]- index < 1 or visited[lst[2*k-2]- index]:
            pass
        else:
            visited[lst[2*k-2]-index] = True
            d_sum += index +1
            p -= 1
        if p == 0:
            break

        if lst[2*k-2]+index>n or visited[lst[2*k-2]+index]:
            pass
        else:
            visited[lst[2*k-2]+index] = True
            d_sum += index +1
            p -= 1
        
        index += 1 
    return d_sum                   # 좌측 먼저 채우는 순서

def fill_place_right(k, lst, visited):
    index = 0
    d_sum = 0
    p = lst[2*k-1]
    while p != 0:
        if lst[2*k-2]+index>n or visited[lst[2*k-2]+ index]:
            pass
        else:
            visited[lst[2*k-2]+index] = True
            d_sum += index +1
            p -= 1
        
        if p == 0:
            break
        
        if lst[2*k-2]- index < 1 or visited[lst[2*k-2]-index]:
            pass
        else:
            visited[lst[2*k-2]-index] = True
            d_sum += index +1
            p -= 1            # 우측 우선
        
        index += 1
    return d_sum         


for tc in range(1,T+1):
    n = int(input())
    n1, p1 = map(int, input().split())
    n2, p2 = map(int, input().split())
    n3, p3 = map(int, input().split())

    test_order = [1,2,3]
    test_case = [[1,2,3],[ 1,3,2] ,[2,1,3], [2,3,1] ,[3,1,2] ,[3,2,1]] # 순열 어케 만드는지 생각 안나서 그냥 다 노가다 함

    data_lst = [n1,p1,n2,p2,n3,p3]

    ans = 60* 20 # 문제 조건에 의한 maximum
    for i in test_case:
        x = fill_place(i,data_lst)
        if ans >  x:
            ans = x
    
    print(f'#{tc} {ans}')
