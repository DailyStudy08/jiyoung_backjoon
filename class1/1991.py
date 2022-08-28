import sys
input = sys.stdin.readline

n = int(input())
dic = {}

def preorder(node):
    if node == 0:
        return

    print(node, end= '')
    preorder(dic[node][0])
    preorder(dic[node][1])

def inorder(node):
    if node == 0:
        return
    inorder(dic[node][0])
    print(node, end='')
    inorder(dic[node][1])

def postorder(node):
    if node == 0:
        return
    postorder(dic[node][0])
    postorder(dic[node][1])
    print(node, end='')




for i in range(n):
    data = input().split()
    if data[1]== '.' and data[2] == '.':
        dic[data[0]] = (0,0)
    elif data[1]== '.':
        dic[data[0]] = (0, data[2])
    elif data[2] == '.':
        dic[data[0]] = (data[1], 0)
    else:
        dic[data[0]] = (data[1], data[2])


preorder('A')
print()
inorder('A')
print()
postorder('A')
