
x,y = 0,0
dir_num = 0
mapper = {
    "N":0,
    "E":1,
    "S":2,
    "W":3
}

dxs = [0,1,0,-1]
dys = [1,0,-1,0]




def move(x,y,dir_num):
    orders = input()
    time=0
    for order in orders:
        if order=="L":
            dir_num = (dir_num-1+4)%4
            time+=1
        elif order=="R":
            dir_num = (dir_num+1)%4
            time+=1
        else:
            x = x+ dxs[dir_num]
            y = y+ dys[dir_num]
            time+=1
        
        if x==0 and y==0:
            return time
            
    if x!=0 or y!=0:
        return -1
print(move(x,y,dir_num))

    
