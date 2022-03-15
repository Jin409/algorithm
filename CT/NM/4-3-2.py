n = int(input())
locations = [0]*201
#0부터 100은 -100~-1 / 101은 0 / 102부터 201 까지는 1~100

def move(x,d,n):
    if d=="L":
        dir_num = -1
    else:
        dir_num = 1

    locations[n]+=1
    
    for i in range(x):
        n += dir_num
        locations[n]+=1
    return n

now = 101
locations[now]+=1

for i in range(n):
    x,d = input().split()
    x = int(x)
    now = move(x,d,now)


before=False
cnt=0

for i in range(len(locations)):
    if locations[i]>=2:
        if before:
            cnt+=1
        else:
            before = True
    else:
        before = False

print(cnt)

    
