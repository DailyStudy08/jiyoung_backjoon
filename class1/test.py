dic = {'C':'a', 'C#':'b' , 'D':'c', 'D#':'d', 'E':'e', 'F':'f','F#':'g', 'G':'h', 'G#':'i','A':'j','A#':'k', 'B':'l', 'E#':'m'}

def codes_to_int(code_str):
    int_str = ''
    for i in range(len(code_str)):
        if i == len(code_str)-1:
            if code_str[i] == '#':
                continue
            else:
                int_str += dic[code_str[i]]
        else:
            if code_str[i] == '#':
                continue
            else:
                if code_str[i+1] == '#':
                    int_str += dic[code_str[i]+code_str[i+1]]
                else:
                    int_str += dic[code_str[i]]
    return int_str


def solution(m, musicinfos):
    
    answer = '(None)'
    time_lst = []
    title_lst =[]
    codes_lst =[]
    counting_index = 0
    index_lst = []

    for music in musicinfos:
        music_info = music.split(',')
        
        start_time = music_info[0].split(':')
        end_time = music_info[1].split(':')
        
        time_minutes = 60*(int(end_time[0]) - int(start_time[0])) + (int(end_time[1]) - int(start_time[1]))
        
        time_lst.append(time_minutes)
        title_lst.append(music_info[2])
        
        codes = music_info[3]
        int_codes = codes_to_int(codes)
        play_once_time = len(int_codes)
        
        play_codes = ''
        time = 0
        while time !=time_minutes:
            now_play = time%play_once_time
            play_codes += int_codes[now_play]
            time +=1
        
        codes_lst.append(play_codes)
        index_lst.append(counting_index)
        counting_index += 1
    
    max_minute = 0
    min_index = len(time_lst)
    
    int_str_m = codes_to_int(m)
    
    for i in range(len(time_lst)):
        if int_str_m in codes_lst[i]:
            if time_lst[i] >max_minute:
                answer = title_lst[i]
                max_minute = time_lst[i]
                min_index = index_lst[i]
            elif time_lst[i] == max_minute:
                if index_lst[i] < min_index:
                    answer = title_lst[i]
                    max_minute = time_lst[i]
                    min_index = index_lst[i]
            
    return answer