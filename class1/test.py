T = int(input())

def merge_sort(lst):
    if len(lst) == 1:
        return lst

    length = len(lst)
    middle = length//2

    left_lst = lst[:length//2]
    right_lst = lst[length//2:]

    left_lst = merge_sort(left_lst)
    right_lst = merge_sort(right_lst)

    return merge(left_lst,right_lst)


def merge(left, right):
    result_lst = []
    global cnt
    if left and right:
        if left[-1] > right[-1]:
            cnt += 1
    
    left_index = 0
    right_index = 0

    while left_index < len(left) or right_index < len(right):
        if left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                result_lst.append(left[left_index])
                left_index +=1
            else:
                result_lst.append(right[right_index])
                right_index +=1
        elif left_index < len(left):
            result_lst.append(left[left_index])
            left_index += 1
        elif right[right_index]:
            result_lst.append(right[right_index])
            right_index +=1
    
    return result_lst


for tc in range(1,T+1):
    n = int(input())
    ans_lst =[]
    want_sorted_lst = list(map(int, input().split()))
    cnt = 0
    merge_lst =merge_sort(want_sorted_lst)

    print(f'#{tc} {merge_lst[n//2]} {cnt}')