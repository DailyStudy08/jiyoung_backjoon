import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(100000)

n = int(input())
inorder = list(map(int,input().split())) #left , center, right
postorder = list(map(int,input().split())) #left, right, center



dic_in = {}
for i in range(n):
    dic_in[inorder[i]] = i

def preorder(range_min,range_max, post_min, post_max):
    if range_min > range_max or post_min > post_max:
        return

    root = postorder[post_max]
    print(root, end = ' ')
    left = dic_in[root] - range_min 
    right = range_max - dic_in[root]
    
    preorder(range_min ,dic_in[root]-1, post_min, post_min+left-1)
    preorder(dic_in[root]+1, range_max, post_max-right, post_max-1)

preorder(0,n-1,0, n-1)
# pivot_index = inorder.index(postorder[-1])

# q = deque([(pivot_index,0,n)])
# tree = [[-1,-1] for _ in range(n+1)]

# while q:
#     cur = q.popleft()

#     now = -1
#     left_pivot_index = -1
#     for i in range(cur[1], cur[0]):
#         if now < dic_post[inorder[i]]:
#             now = dic_post[inorder[i]]
#             left_pivot_index = i
#     if now == -1:
#         pass
#     else:
#         tree[inorder[cur[0]]][0] = inorder[left_pivot_index]
#         q.append((left_pivot_index, cur[1], cur[0]))
    
#     now = -1
#     right_pivot_index = -1
#     for i in range(cur[0]+1, cur[2]):
#         if now < dic_post[inorder[i]]:
#             now = dic_post[inorder[i]]
#             right_pivot_index = i
#     if now == -1:
#         pass
#     else:
#         tree[inorder[cur[0]]][1] = inorder[right_pivot_index]
#         q.append((right_pivot_index, cur[0]+1, cur[2]))

# def preorder(cur):
#     print(cur , end = ' ')
#     if tree[cur][0] != -1:
#         preorder(tree[cur][0])
    
#     if tree[cur][1] != -1:
#         preorder(tree[cur][1])


# preorder(postorder[-1])

    




    # print(inorder[pivot_index], end = ' ')

    # cur = -1
    # left_pivot_index = -1

    # for i in range(left_min, pivot_index):
    #     if cur < dic_post[inorder[i]]:
    #         cur = dic_post[inorder[i]]
    #         left_pivot_index = i

    # if cur == -1:
    #     pass
    # else:
    #     preorder(left_min, pivot_index, left_pivot_index)

    # cur = -1
    # right_pivot_index = -1
    # for i in range(pivot_index+1, right_max):
    #     if cur < dic_post[inorder[i]]:
    #         cur = dic_post[inorder[i]]
    #         right_pivot_index = i
    
    
    
    # if cur == -1:
    #     pass
    # else:
    #     preorder(pivot_index+1, right_max, right_pivot_index)

# preorder(0,n,pivot_index)


# left_temp = inorder[:pivot_index]
# right_temp = inorder[pivot_index+1:]
# for i in range(n):
#     dic_in[inorder[i]] = i
# dic_in = {}

