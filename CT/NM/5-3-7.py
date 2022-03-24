orders = list(input())


mapper = {
    "N":0,
    "E":1,
    "S":2,
    "W":3
}

dir_num = 0

dxs = [0,1,0,-1]
dys = [1,0,-1,0]
x,y = 0,0
result_time = 0
is_arrived = False

for order in orders:
    if order=="R":
        dir_num = (dir_num+1)%4
    elif order=="L":
        dir_num = (dir_num-1+4)%4
    else:
        x += dxs[dir_num]
        y += dys[dir_num]
    
    result_time +=1 

    if x==0 and y==0 :
        is_arrived=True
        break

if is_arrived:
    print(result_time)
else:
    print(-1)