dice_array = list(map(int, input().split()))
dice_array.reverse()

graph = [[] for _ in range(351)]

graph[40] = [-1]
graph[0] = [2]

for i in range(1,20):
    graph[2*i] = [2*i+2]



graph[10].append(130)
graph[130].append(160)
graph[160].append(190)
graph[190].append(250)
graph[20].append(220)
graph[220].append(240)
graph[240].append(250)
graph[30].append(280)
graph[280].append(270)
graph[270].append(260)
graph[260].append(250)
graph[250].append(300)
graph[300].append(350)
graph[350].append(40)

answer = 0


def dfs(cur_arr , score, dice):
    if len(dice) == 0:
        global answer

        if score > answer :
            answer = score
        
        return
    
    
    for d in range(4):
        k = dice.pop()
        tmp_num = cur_arr[d]
        flag = False

        if cur_arr[d] == -1:
            dice.append(k)
            continue


        if cur_arr[d] == 10 or cur_arr[d] == 20 or cur_arr[d] == 30:
            cur_arr[d] = graph[cur_arr[d]][1]
            l = k-1
        else:
            l = k

        for a in range(l):
            cur_arr[d] = graph[cur_arr[d]][0]
            if cur_arr[d] == -1:
                break
        
        if not cur_arr[d] == -1:
            for c in range(4):
                if c != d and cur_arr[c] == cur_arr[d]:
                    cur_arr[d] = tmp_num
                    dice.append(k)
                    flag = True
                    break
        
        if flag:
            continue
        


        if cur_arr[d] > 100:
            score += cur_arr[d]//10
        elif cur_arr[d] == -1:
            pass
        else:
            score += cur_arr[d]

        dfs(cur_arr, score, dice)

        if cur_arr[d] > 100:
            score -= cur_arr[d]//10
        elif cur_arr[d] == -1:
            pass
        else:
            score -= cur_arr[d]

        cur_arr[d] = tmp_num
        dice.append(k)


dfs([0,0,0,0], 0, dice_array)

print(answer)

    
        
