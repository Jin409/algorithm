n = int(input())

arr = [
    input()
    for _ in range(n)
]

start = int(input())

#시작하는 곳의 인덱스를 찾음.
def start_point(start):
    if start<=n:
        return 0, start-1,0
    elif start <=n*2:
        return start-1-n, n-1,1
    elif start <= n*3:
        return n-1, n*3-start,2
    else:
        return n*4-start, 0,3


mapper = {
    "D":0,
    "L":1,
    "U":2,
    "R":3
}

def in_range(x,y):
    return x<n and y<n and x>=0 and y>=0


# 거울이 /라면 (dir_num-3+4)%4 거울이 \ 라면..? (dir_num-1+4)%4
#x,y는 start_point의 결과값

dxs = [1,0,-1,0]
dys = [0,-1,0,1]

cnt = 1

def simulate(x,y,dir_num):
    global cnt
    while True:
        if arr[x][y]=="/":
            dir_num = dir_num ^ 1 
        else:
            dir_num = 3 - dir_num
        nx = x+dxs[dir_num]
        ny = y+dys[dir_num]
        if in_range(nx,ny):
            x = nx
            y = ny
            cnt+=1
        else:
            break

x,y,dir_num = start_point(start)
simulate(x,y,dir_num)
print(cnt)

