import sys

n,m = map(int,input().split())
arr1 = [] #arr를 시간으로 ..?  위치로..? 시간!
arr2 = []

#시작하는 위치, 방향, 시간
def move1(s,d,t):
    if d=="L":
        dir_num = -1
    else:
        dir_num = 1
    
    move_num = s

    for i in range(t):
        arr1.append(move_num)
        move_num += dir_num

    return move_num

def move2(s,d,t):
    if d=="L":
        dir_num = -1
    else:
        dir_num = 1
    
    move_num = s

    for i in range(t):
        arr2.append(move_num)
        move_num += dir_num

    return move_num

now = 0

for i in range(n):
    #d는 방향 t는 몇 초동안
    d,t = input().split()
    t = int(t)
    now = move1(now,d,t)

now = 0

for i in range(m):
    #d는 방향 t는 몇 초동안
    d,t = input().split()
    t = int(t)
    now = move2(now,d,t)

answer = -1
for i in range(1,len(arr1)):
    if arr1[i]==arr2[i]:
        answer = i
        break

print(answer)
