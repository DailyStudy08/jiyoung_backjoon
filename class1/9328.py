import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def bfs(starting_point):
    q = deque([starting_point])
    di = [-1,1, 0,0]
    dj = [0,0,-1,1]
    global flag
    flag = False
    while q:
        cur = q.popleft()

        for d in range(4):
            next = (cur[0]+ di[d] , cur[1]+dj[d])
            if 0<= next[0] <= h+1 and 0 <= next[1] <= w+1:
                if visited[next[0]][next[1]] < 1 and mat[next[0]][next[1]] != 1 :
                    if mat[next[0]][next[1]] ==0:
                        visited[next[0]][next[1]] = 1
                        q.append(next)
                    elif  mat[next[0]][next[1]] == 1:
                        continue
                    elif mat[next[0]][next[1]] ==3:
                        visited[next[0]][next[1]] = 1
                        q.append(next)
                        global ans
                        ans += 1
                        mat[next[0]][next[1]] = 0
                    elif 65 <= mat[next[0]][next[1]] <=90:
                        for key in key_lst:
                            if key -32 == mat[next[0]][next[1]]:
                                visited[next[0]][next[1]] =1
                                mat[next[0]][next[1]] = 0
                                q.append(next)
                                break
                    elif 97 <= mat[next[0]][next[1]] <= 122:
                        key_lst.append(mat[next[0]][next[1]])
                        # for i in range(h):
                        #     if mat[next[0]][next[1]] -32 == mat[i][0]:
                        #         starting_point.append((i,0))
                        #     if mat[next[0]][next[1]] - 32 == mat[i][w-1]:
                        #         starting_point.append((i,w-1))
                        
                        # for i in range(w):
                        #     if mat[next[0]][next[1]] -32 == mat[0][i]:
                        #         starting_point.append((0,i))
                        #     if mat[next[0]][next[1]] -32 == mat[h-1][i]:
                        #         starting_point.append((h-1,i))
                        # q = deque([starting_point])
                        # visited = [[0]*(w+2) for _ in range(h+2)]
                        mat[next[0]][next[1]] = 0
                        flag = True
                        break

for tc in range(T):
    h,w = map(int, input().split())
    mat = [[0]*(w+2) for _ in range(h+2)]
    # starting_point = []
    key_lst = []
    ans = 0
    for i in range(h):
        s = input().strip()
        for j in range(len(s)):
            # 알파벳 소문자, 대문자, * 벽 , . 이동 가능 , $ 문서
            if s[j] == '*':
                mat[i+1][j+1] = 1
            elif s[j] == '.':
                # if i == 0 or i== h-1 or j == 0 or j == len(s)-1:
                #     starting_point.append((i,j))
                mat[i+1][j+1] = 0
            elif s[j] == '$':
                # if i == 0 or i== h-1 or j == 0 or j == len(s)-1:
                #     starting_point.append((i,j))
                #     ans += 1
                #     mat[i][j] = 0
                # else:
                mat[i+1][j+1] = 3
            elif 65<= ord(s[j]) <= 90:   # 대문자
                mat[i+1][j+1] = ord(s[j])
            elif 97<= ord(s[j]) <= 122:  # 소문자
                mat[i+1][j+1] = ord(s[j])
                # if i == 0 or i== h-1 or j == 0 or j == len(s)-1:
                #     starting_point.append((i,j))
                #     key_lst.append(mat[i][j])
    
    s = input().strip()
    
    
    

    for c in s:
        key_lst.append(ord(c))

    # for key in key_lst:
    #     for i in range(h):
    #         if key -32 == mat[i][0]:
    #             starting_point.append((i,0))
    #         if key - 32 == mat[i][w-1]:
    #             starting_point.append((i,w-1))
        
    #     for i in range(w):
    #         if key -32 == mat[0][i]:
    #             starting_point.append((0,i))
    #         if key -32 == mat[h-1][i]:
    #             starting_point.append((h-1,i))
    flag = True
    while flag:
        visited = [[0]*(w+2) for _ in range(h+2)]
        bfs((0,0))

    
    print(ans)







                


                




