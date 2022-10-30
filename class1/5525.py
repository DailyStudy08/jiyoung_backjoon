import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()
cnt = 0
i = 1
pattern = 0
while i < m:
    if s[i-1] == 'I' and s[i] == 'O' and s[i+1] == 'I':
        pattern += 1

        if pattern == n:
            pattern -= 1
            cnt += 1        
        i += 1
    else:
        pattern = 0
    
    i += 1

print(cnt)
