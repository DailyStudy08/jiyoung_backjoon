N = int(input())

str_lst = []

for i in range(N):
    int_lst = list(map(int,input().split()))
    M = int_lst[0]
    average = 0
    sum_lst =0
    cnt =0
    for j in int_lst[1:]:
        sum_lst += j
        cnt +=1
    average = sum_lst/cnt
    average_over_cnt = 0
    for j in int_lst[1:]:
        if average < j:
            average_over_cnt += 1
    s = round(100*average_over_cnt/len(int_lst[1:]),3)
    print(f'{st:.3f}%')