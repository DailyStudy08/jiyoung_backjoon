nm_list = list(map(int,input().split()))

N = nm_list[1]
M = nm_list[0]

era_chae = [False]*(N+1)

for idx, i in enumerate(era_chae):
    if idx == 0 or idx == 1:
        continue

    if i == False :
        n = 1
        while idx*n <= N:
            era_chae[idx*n] = True
            n += 1
        
        if idx>=M:
            print(idx)