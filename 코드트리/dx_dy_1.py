n,m = map(int,input().split())

arr = [
    [0]*n
    for _ in range(n)
]

dxs = [0,1,-1,0]
dys = [-1,0,0,1]

def in_range(x,y):
    return x<n and y<n and y>=0 and x>=0

for _ in range(m):
    cnt = 0
    x,y = map(int,input().split())
    x-=1
    y-=1
    if in_range(x,y):
        arr[x][y] = 1
        for i in range(4):
            nx = x+dxs[i]
            ny = y+dys[i]
            if in_range(nx,ny) and arr[nx][ny]==1:
                cnt+=1
    if cnt==3:
        print(1)
    else:
        print(0)
