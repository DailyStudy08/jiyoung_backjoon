import sys
input = sys.stdin.readline

n,m, k = map(int, input().split())


arr = []
for i in range(n):
    arr.append(int(input()))

seg_tree = [0]*(4*n)

def init(start, end, index):
    if start == end:
        seg_tree[index] = arr[start]
        return seg_tree[index]
    
    mid = (start+end)//2
    seg_tree[index] = (init(start, mid,index*2) * init(mid+1, end, index*2 +1))%1000000007
    return seg_tree[index]

def cal_sum(start, end, index, left, right):
    if left > end or right < start:
        return 1
    
    if start >= left and end <=right:
        return seg_tree[index]
    
    mid = (start + end)//2
    return cal_sum(start, mid, index*2, left, right) * cal_sum(mid+1, end, index*2 + 1, left, right)%1000000007


def update(start, end, index, target, target_val ):
    if target < start or target> end:
        return
    
    
    if start == end:
        seg_tree[index] = target_val
        return
    
    mid = (start + end)//2
    update(start, mid, index*2 , target, target_val )
    update(mid+1, end , index*2+1 , target, target_val)

    seg_tree[index] = seg_tree[index*2]*seg_tree[index*2+1]%1000000007


init(0, n-1, 1)


for i in range(m+k):
    a,b,c = map(int, input().split())
    if a == 1:
        update(0,n-1, 1, b-1, c )
    else:
        print(cal_sum(0,n-1,1,b-1,c-1))
