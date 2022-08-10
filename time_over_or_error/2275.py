import sys
input = sys.stdin.readline
# f = open('input.txt','r')
# input = f.readline


N, H = map(int, input().split())
dic_graph = {}  # 그래프의 표현 조금 특수하게 조상까지 기록하도록 하자
height_array = [0]*(N+1) # 정점까지 height ... 애매한건 input 이 혹시 해당 정점이 안나왔는데 부모 정점으로 먼저 나올 수도 있나? 
# 일단 무시하고 키에러 뜨면 그때 고려 
over_h_lst = []
g_lst = [0]*(N+1) #각 정점에서 가중치 = 줄일 수 있는 가중치

for i in range(1,N+1):
    p, g = map(int, input().split()) # 부모 노드와  가중치
    
    if p == 0 :
        dic_graph[i] = [1]
    else:
        dic_graph[i] = dic_graph[p] +[i]  # dictionary에 루트까지 어떻게 이어지는지 기록 
    
    height_array[i] = height_array[p] + g

    if height_array[i] > H:
        over_h_lst.append(i)  # H 초과하는 정점의 정점 번호 기억 0번 부터 시작이니 +1 주의는 그냥 번호 맞춤
    
    g_lst[i] = g

ans = 0


while over_h_lst != []:  # falsy 를 사용할 수도 있을듯 
    count_lst = [0]*(N+1)   # h 보다 큰 정점의 조상인 경우 count +=
    for i in over_h_lst:
        for a in dic_graph[i]:
            count_lst[a] += 1
    
    index_lst = [x for x in range(N+1)]
    count_index = zip(index_lst, count_lst)
    count_index = sorted(count_index, key= lambda x : -x[1]) # count 로 역순 정렬

    for x in count_index:
        if g_lst[x[0]] != 0:
            height_array[x[0]] -= 1
            g_lst[x[0]] -= 1
            ans += 1                                                            ## 36~ 57 요거 계속 갱신하는게 너무 마음에 안드는데, tree 구조 개념과
            break                                                               ## 표현이 자연스럽지 않은듯 하다.. 무조건 시간 초과 날듯
    
    over_h_lst = []                                                             ## 최악의 경우 n^2 *logn 정도?
    for i in range(1,N+1):
        tmp_lst = dic_graph[i]
        if len(tmp_lst) == 1:
            p = 0
        else : 
            p = tmp_lst[-2] 
        g = g_lst[i]

        height_array[i] = height_array[p] +g
        if height_array[i] > H:
            over_h_lst.append(i)


print(ans)