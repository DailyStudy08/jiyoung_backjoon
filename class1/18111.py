import sys
input = sys.stdin.read
output = sys.stdout.write
# f =  open('input.txt', 'r')
# input = f.read


### 맞힌 사람을 보니 Dp 를 사용하면 시간을 많이 줄일 수 있는 것 같네요.

def sol():
    n , m , b , *mat = list(map(int, input().split()))

    # mat.sort()

    index = 0
    can_min = min(mat)
    can_max = int((sum(mat)+ b)/len(mat))
    time = 0
    height = 0


    for i in mat:
        if i < can_min:
            time += can_min - i
        elif i > can_min:
            time += 2*(i -can_min)

    for i in range(can_min, can_max+1):
    #for i in range(257):
        case_time = 0
        # cnt = 0
        # min_cnt = 0
        for j in mat:
            if j < i:
                case_time += i - j
                # min_cnt += 1
            else:
                case_time += 2*(j -i)
                # cnt += 1
        # if cnt + b <min_cnt:
        #     continue
        
        if case_time <= time:
            time = case_time
            height = i

    s = str(time) + ' '+ str(height)
    return s


output(sol())

# commit conflit?


# for i in range(len(mat)-1):
#     if mat[i] != mat[i+1]:
#         index = i
#         break

# while (index+1) < sum([x - mat[index] for x in mat[index+1:]]):
#     mat[:index+1] = [x+1 for x in mat[:index+1]]
#     time += index+1
#     for i in range(index, len(mat)-1):
#         index = 


# f.close()