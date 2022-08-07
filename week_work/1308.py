import sys
input = sys.stdin.readline
output = sys.stdout.write
# f =  open('input.txt', 'r')
# input = f.readline

lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
yoon_month = [31,29,31,30,31,30,31,31,30,31,30,31]
month = [31,28,31,30,31,30,31,31,30,31,30,31]

def cal_day(lst1,lst2):
    s ='D-'
    cnt = 0
    while lst1 != lst2:
        lst1[2] += 1
        cnt += 1
        if (lst1[0]%4 == 0 and lst1[0]%100 != 0) or lst1[0]%400 == 0:
            if lst1[2] > yoon_month[lst1[1]-1]:
                lst1[2] -= yoon_month[lst1[1]-1]
                lst1[1] += 1
                if lst1[1] >12:
                    lst1[1] -= 12
                    lst1[0] += 1
        else:
            if lst1[2] > month[lst1[1]-1]:
                lst1[2] -= month[lst1[1]-1]
                lst1[1] += 1
                if lst1[1] >12:
                    lst1[1] -= 12
                    lst1[0] += 1
    s = s + str(cnt)
    print(s)


if lst1[0]+1000 ==lst2[0]:
    if lst1[1]< lst2[1]:
        print('gg')
    elif lst1[1] == lst2[1]:
        if lst1[2] <= lst2[2]:
            print('gg')
        else:
            cal_day(lst1,lst2)
    else:
        cal_day(lst1,lst2)
elif lst1[0]+1000 < lst2[0]:
    print('gg')
else:
    cal_day(lst1,lst2)




