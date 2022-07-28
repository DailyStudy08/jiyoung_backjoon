from collections import deque   #... 그냥 list 보다 빠르다고 해서 쓰려고 했는데, iterable 을 넣어버리면 각 원소를 큐에다가 집어넣네요..


def in_bfs(length, mat, lst, visited):
    temp_lst = []
    while lst:
        v = lst.pop(0)

        if v[0] < 0 or v[0] >N-1:
            continue
        elif v[1]<0 or v[1] >N-1:
            continue

        if not visited[v[0]][v[1]]:
            if now_shark_size >= mat[v[0]][v[1]]:
                visited[v[0]][v[1]] = True
                if now_shark_size > mat[v[0]][v[1]] and mat[v[0]][v[1]] != 0:
                    mat[v[0]][v[1]] = 0
                    now_pos = v[:] 
                    return length , mat, now_pos, True   # 요 경우가 정상적으로 먹은 경우
                else :
                    temp_lst.append([v[0]-1, v[1]]) # 위
                    temp_lst.append([v[0], v[1]-1]) # 왼
                    temp_lst.append([v[0], v[1]+1]) # 오 
                    temp_lst.append([v[0]+1, v[1]]) # 아
            else :
                continue
        else:
            continue
    #정상적으로 먹은 경우에 안 걸리고 queue 빌 때까지 돌았다면?
    temp_lst = list(set([tuple(item) for item in temp_lst]))        # ................. 2차원 배열 중복제거는 이렇게 할 수도 있다고...... 도대체 왜 이렇게 까지 왔지..?
    temp_lst = sorted(temp_lst, key= lambda x: (x[0],x[1]))         #... python custom 정렬은 이런식으로 한다고 하네요.. 왜 여기까지 왔는지 모르겠지만  y 작을수록 ... 그 후 x 작을수록

    if temp_lst:
        return in_bfs(length+1, mat, temp_lst, visited)
    else:
        return 0,0,0,False # 파이썬은 혹시 튜플이니까 return 인자 수 각 경우마다 다르게 할 수 도 있나? ... 찾아봐야할 부분



def modified_bfs(mat, now_pos, now_shark_size):
    visited = [[False]*N for i in range(N)]
    queue = []
    queue.append([now_pos[0], now_pos[1]]) 
    visited[now_pos[0]][now_pos[1]] = True
    length = 0

    queue.append([now_pos[0]-1, now_pos[1]]) # 위
    queue.append([now_pos[0], now_pos[1]-1]) # 왼
    queue.append([now_pos[0], now_pos[1]+1]) # 오
    queue.append([now_pos[0]+1, now_pos[1]]) # 아

    return in_bfs(length+1, mat, queue, visited)

# 파이썬 무조건 함수는 위에 선언 해야하는 구조였던가?

N = int(input())
mat = []
now_pos = list()
for i in range(N):
    mat.append(list(map(int,input().split())))

# 0~ 8 , 0~8 // y,x 순서 , y는 감소가 위쪽 x는 증가가 오른쪽  신경쓰고
for i in range(N):
    for j in range(N):
        if mat[i][j] == 9:
            now_pos = [i,j]
            mat[i][j] = 0


now_shark_size = 2
eat_count = 0
time = 0

while True:
    length, mat, now_pos, not_end = modified_bfs(mat,now_pos,now_shark_size)
    if not_end:
        eat_count +=1
        time += length
        if eat_count == now_shark_size:
            eat_count = 0
            now_shark_size += 1
    else :
        break

print(time)
