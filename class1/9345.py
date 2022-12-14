import sys
input = sys.stdin.readline


T = int(input())


def init(start, end, index):
    if start == end:
        seg_tree[index] = arr[start]
        return seg_tree[index]
    
    mid = (start+end)//2
    seg_tree[index] = min(init(start, mid,index*2),init(mid+1, end, index*2 +1))
    return seg_tree[index]

def cal_min(start, end, index, left, right):
    if left > end or right < start:
        return 100000
    
    if start >= left and end <=right:
        return seg_tree[index]
    
    mid = (start + end)//2
    return min(cal_min(start, mid, index*2, left, right),cal_min(mid+1, end, index*2 + 1, left, right))


def update(start, end, index, target, target_val):
    if target < start or target> end:
        return
    
    seg_tree[index] += target_val
    if start == end:
        arr[start] += target_val
        return
    
    mid = (start + end)//2
    update(start, mid, index*2 , target, target_val)
    update(mid+1, end , index*2+1 , target, target_val)

for tc in range(1,T+1):
    n,k = map(int, input().split())

    arr = [i for i in range(1, n+1)]
    seg_tree = [0]*(4*n)



init(0, n-1, 1)


for i in range(m+k):
    a,b,c = map(int, input().split())
    if a == 1:
        update(0,n-1, 1, b-1, c - arr[b-1])
    else:
        print(cal_sum(0,n-1,1,b-1,c-1))
