from collections import deque

n, m = map(int, input().split())

mat = [[0]*m for _ in range(n)]

red = (0,0)
blue = (0,0)
hole = (0,0)


for i in range(n):
    word = input()
    for j in range(m):
        if word[j] == '#':
            mat[i][j] = 1
        elif word[j] == '.':
            mat[i][j] = 0
        elif word[j] == 'B':
            blue = (i,j)
        elif word[j] == 'R':
            red = (i,j)
        elif word[j] == 'O':
            hole = (i,j)



def bfs(cur_red, cur_blue, cur_hole):
    q = deque()
    q.append((cur_red, cur_blue, 0))
    ans = -1

    red_hole = False
    blue_hole = False
    hole = cur_hole

    while q:
        cur = q.popleft()

        cur_red = cur[0]
        cur_blue = cur[1]
        cur_cnt = cur[2]

        if cur_cnt > 10:
            ans = -1
            break

        for d in range(4):
            if d == 0:
                if cur_red[1] > cur_blue[1]:
                    for a in range(cur_blue[1], -1, -1):
                        if (cur_blue[0], a) == hole:
                            blue_hole = True
                            break
                        if mat[cur_blue[0]][a] != 0:
                            next_cur_blue = (cur_blue[0], a+1)
                            break
                    for b in range(cur_red[1], -1, -1):
                        if (cur_red[0], b) == hole:
                            red_hole = True
                            break
                        if mat[cur_red[0]][b] != 0 or (cur_red[0],b) == next_cur_blue:
                            next_cur_red = (cur_red[0], b+1)
                            break
                else:
                    for b in range(cur_red[1], -1, -1):
                        if (cur_red[0], b) == hole:
                            red_hole = True
                            break
                        if mat[cur_red[0]][b] != 0 :
                            next_cur_red = (cur_red[0], b+1)
                            break
                    for a in range(cur_blue[1], -1, -1):
                        if (cur_blue[0], a) == hole:
                            blue_hole = True
                            break
                        if mat[cur_blue[0]][a] != 0 or (cur_blue[0],a) == next_cur_red:
                            next_cur_blue = (cur_blue[0], a+1)
                            break
            elif d== 1:
                if cur_red[1] > cur_blue[1]:
                    for a in range(cur_red[1], n, 1):
                        if (cur_red[0], a) == hole:
                            blue_hole = True
                            break
                        if mat[cur_red[0]][a] != 0:
                            next_cur_red = (cur_red[0], a-1)
                            break
                    for b in range(cur_blue[1], n, 1):
                        if (cur_blue[0], b) == hole:
                            red_hole = True
                            break
                        if mat[cur_blue[0]][b] != 0 or (cur_blue[0],b) == next_cur_red:
                            next_cur_blue = (cur_blue[0], b-1)
                            break
                else:
                    for b in range(cur_blue[1], n, 1):
                        if (cur_blue[0], b) == hole:
                            red_hole = True
                            break
                        if mat[cur_blue[0]][b] != 0 or (cur_blue[0],b) == next_cur_red:
                            next_cur_blue = (cur_blue[0], b-1)
                            break
                    for a in range(cur_red[1], n, 1):
                        if (cur_red[0], a) == hole:
                            blue_hole = True
                            break
                        if mat[cur_red[0]][a] != 0:
                            next_cur_red = (cur_red[0], a-1)
                            break
            elif d== 2:
                if cur_red[0] > cur_blue[0]:
                    for a in range(cur_blue[0], -1, -1):
                        if (a, cur_blue[1]) == hole:
                            blue_hole = True
                            break
                        if mat[a][cur_blue[1]] != 0:
                            next_cur_blue = (a+1, cur_blue[1])
                            break
                    for b in range(cur_red[0], -1, -1):
                        if (b, cur_red[0]) == hole:
                            red_hole = True
                            break
                        if mat[b][cur_red[1]] != 0 or (b, cur_red[1]) == next_cur_blue:
                            next_cur_red = (b+1, cur_red[0])
                            break
                else:
                    for b in range(cur_red[0], -1, -1):
                        if (b, cur_red[0]) == hole:
                            red_hole = True
                            break
                        if mat[b][cur_red[1]] != 0 or (b, cur_red[1]) == next_cur_blue:
                            next_cur_red = (b+1, cur_red[0])
                            break
                    for a in range(cur_blue[0], -1, -1):
                        if (a, cur_blue[1]) == hole:
                            blue_hole = True
                            break
                        if mat[a][cur_blue[1]] != 0:
                            next_cur_blue = (a+1, cur_blue[1])
                            break
            elif d == 3:
                if cur_red[0] > cur_blue[0]:
                    for a in range(cur_red[0], n, 1):
                        if (a,cur_red[1]) == hole:
                            blue_hole = True
                            break
                        if mat[a][cur_red[1]] != 0:
                            next_cur_red = (a-1, cur_red[1])
                            break
                    for b in range(cur_blue[0], n, 1):
                        if (b,cur_blue[1]) == hole:
                            red_hole = True
                            break
                        if mat[b][cur_blue[1]] != 0 or (b,cur_blue[1]) == next_cur_red:
                            next_cur_blue = (b-1, cur_blue[1])
                            break
            
            if red_hole and blue_hole == False:
                ans = cur_cnt +1
                break
            
            if red_hole or blue_hole :
                pass
            elif cur_red == next_cur_red and cur_blue == next_cur_blue :
                pass
            else:
                q.append((next_cur_red, next_cur_blue, cur_cnt+1))
                red_hole = False
                blue_hole = False
        if ans != -1:
            break
    return ans
            


print(bfs(red, blue, hole))




