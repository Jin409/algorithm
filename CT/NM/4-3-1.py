# 최대로 선분이 많이 겹치는 경우

n = int(input())
lines = []
check_line = [0]*101 #최대가 100이므로

for i in range(n):
    x = tuple(map(int,input().split()))
    lines.append(x)
    check_line

for i in range(len(lines)):
    s,e = lines[i]
    for j in range(s,e+1):
        check_line[j] +=1

print(max(check_line))