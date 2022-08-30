import sys
input = sys.stdin.readline

v = int(input())
adj_lst = [[] for _ in range(v+1)]
# 거리는 어떻게 기입 하지?
visited = [False] *(v+1)
one_lst = []

def dfs(start, cur, length):
    if len(adj_lst[cur]) ==1 and cur != start:
        global tree_r
        global re_start
        if length > tree_r:
            tree_r = length
            re_start = cur
        return    # dfs 재귀 순회 return 은 항상 헷갈리네 하..  2가지 이상의 루트가 있나? => 아마 아닐듯
    
    for i in adj_lst[cur]:  # i 는 (정점, 거리) 의 튜플
        if not visited[i[0]]:
            visited[i[0]] = True
            dfs(start, i[0],length+i[1])
            visited[i[0]] = False
            
    


for i in range(1,v+1):
    # 정점 번호 순서대로가 아닐 수도 있네
    # 시작은 번호 끝은 -1 나머지는 2개씩 끊어서
    tmp_lst = list(map(int, input().split()))
    if len(tmp_lst) == 4:
        one_lst.append(tmp_lst[0])
    
    for j in range((len(tmp_lst)-2)//2):
        adj_lst[tmp_lst[0]].append((tmp_lst[2*j+1], tmp_lst[2*j +2]))  #  ㅁ // 1 1 // 2 2 // 3 3 // 4 4 // ㅁ 느낌 
    
tree_r = 0
root_to_leaf = [0]*(v+1)

tmp_length = 0
re_start = 0

# 시간 초과
# for i in range(len(one_lst)):
#     for j in range(i+1, len(one_lst)):
#         visited = [False] *(v+1)
#         dfs(one_lst[i],one_lst[j],0)
#         if tree_r < tmp_length:
#             tree_r = tmp_length
visited[one_lst[0]] = True


dfs(one_lst[0], one_lst[0], 0)

visited = [False] *(v+1)
visited[re_start] = True
tree_r = 0
dfs(re_start, re_start, 0)



# is_root_to_one_path = False

# if len(adj_lst[3])== 1:
#     is_root_to_one_path = True


# if is_root_to_one_path:
#     tree_r = max(root_to_leaf)
# else:
#     for i in range(len(root_to_leaf)):
#         for j in range(i+1,len(root_to_leaf)):
#             tmp_length = root_to_leaf[i] + root_to_leaf[j]
#             if tmp_length > tree_r:
#                 tree_r = tmp_length

print(tree_r)


