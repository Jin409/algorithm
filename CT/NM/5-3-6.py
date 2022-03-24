n = int(input())

mapper = {
    "W":0,
    "S":1,
    "N":2,
    "E":3
}

dxs = [0,-1,1,0]
dys = [-1,0,0,1]

arr = [
    [0]*n
    for _ in range(n)
]

time_result = 0
x,y = 0,0
is_arrived = False

for i in range(n):
    #방향과 거리를 입력받는다.
    direction,dis = input().split()
    dis = int(dis)
    dir_num = mapper[direction]
    for j in range(dis):
        if is_arrived:
            break
        x += dxs[dir_num]
        y += dys[dir_num]
        time_result+=1
        if x ==0 and y==0:
            is_arrived=True

if not is_arrived:
    print(-1)
else:
    print(time_result)

