import sys
input = sys.stdin.readline

r,c, m = map(int, input().split())
mat = [[[] for _ in range(c+1)] for _ in range(r+1)]
di = [0,-1,1,0,0]
dj = [0,0,0,1,-1]
visited = [[0]*(c+1) for _ in range(r+1)]
shark_lst = []
now_fishing = 0
from_earth = r+1
no_count_lst = []
no_count_index = -1

for i in range(m):
    a,b,s,d,z = map(int,input().split())
    shark_lst.append((a,b,s,d,z))
    if b == 1:
        if from_earth > a:
            from_earth = a
            now_fishing = z
            no_count_index = i





ans = 0

for i in range(1,c+1):
    ans += now_fishing
    if no_count_index != -1:
        no_count_lst.append(no_count_index)
    now_fishing = 0
    from_earth = r+1
    no_count_index = -1
    visited = [[0]*(c+1) for _ in range(r+1)]

    for j in range(m):
        if not j in no_count_lst:
            a,b,s,d,z = shark_lst[j]
            if d == 1 or d==2:
                k = (a+di[d]*s)%(2*(r-1))
                if k== 0:
                    k = 2*(r-1)
                if k > r-1:
                    if d==1:
                        d=2
                    else:
                        d=1
                    a = (r+1) - (k-(r-1))
                else:
                    a= k
            elif d==3 or d==4:
                k = (b+dj[d]*s)%(2*(c-1))
                if k== 0:
                    k = 2*(c-1)
                if k > c-1:
                    if d ==3:
                        d =4
                    else:
                        d =3
                    b = (c+1) - (k-(c-1))
                else:
                    b = k
            
            shark_lst[j] = (a,b,s,d,z)
            
            # 잡아 먹는 경우
            if visited[a][b]:
                if visited[a][b][0] < z:
                    no_count_lst.append(visited[a][b][1])
                    visited[a][b] = (z,j)
                else:
                    no_count_lst.append(j)   
            else:
                visited[a][b] = (z,j)
            
            # 다음 낚시 될 물고기 갱신
            if b==i+1:
                if from_earth == a:
                    if z >now_fishing:
                        now_fishing = z
                        no_count_index = j
                elif from_earth > a:
                    from_earth = a
                    now_fishing = z
                    no_count_index = j
print(ans)


    


