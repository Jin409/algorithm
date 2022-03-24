# 다음 칸이 자리가 없거나, 이미 방문한 경우에는 방향을 틀어야 함.
n,m = map(int,input().split())

arr = [
    [0]*m
    for _ in range(n)
]

def in_range(x,y):
    return x<n and y<m and x>=0 and y>=0

dic_num = 0
x,y = 0,0
num = 1
dxs = [0,1,0,-1]
dys = [1,0,-1,0]

for i in range(n*m):
    arr[x][y]=num
    nx = x+dxs[dic_num]
    ny = y+dys[dic_num]
    if not in_range(nx,ny) or arr[nx][ny]!=0:
        dic_num = (dic_num+1)%4
    x += dxs[dic_num]
    y += dys[dic_num]
    num+=1

for i in range(n):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()