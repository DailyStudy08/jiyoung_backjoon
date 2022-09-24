n = int(input())
a_lst = list(map(int,input().split()))
m = int(input())
m_lst = list(map(int, input().split()))
dic = {}
for i in range(n):
    dic[a_lst[i]] = 1

for i in range(m):
    if dic.get(m_lst[i]):
        print(1)
    else:
        print(0)