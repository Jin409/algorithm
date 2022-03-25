#4칸 중 색칠 된 곳이 3개인 경우.

n,m = map(int,input().split())
arr = [
    [0]*n
    for _ in range(n)
]

dxs = [0,0,-1,1]
dys = [-1,1,0,0]

def in_range(x,y):
    return x<n and y<n and x>=0 and y>=0

def check(x,y):
    cnt=0
    for i in range(4):
        nx = x+dxs[i]
        ny = y+dys[i]
        if in_range(nx,ny) and arr[nx][ny]==1:
            cnt+=1
    return cnt


for i in range(m):
    x,y = map(int,input().split())
    x-=1
    y-=1
    arr[x][y]=1
    if check(x,y)==3:
        print(1)
    else:
        print(0)