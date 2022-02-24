n = int(input())
arr = []
for i in range(n):
    num = list(map(int,input().split()))
    arr.append(num)

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

##########################################################################################



dxs = [0,-1,0,1]
dys = [1,0,-1,0]

def in_range(x,y):
    return x<n and y<n and x>=0 and y>=0 

bomb_list = []
def dfs(x,y,num):
    global cnt
    for dx,dy in zip(dxs,dys):
        nx = x+dx
        ny = y+dy
        if in_range(nx,ny) and not visited[nx][ny]:
            if num==arr[nx][ny]:
                cnt+=1
                visited[nx][ny] = 1
                dfs(nx,ny,num)
    
max_block = 0
for i in range(n):
    for j in range(n):
        cnt=1
        visited[i][j] = 1
        dfs(i,j,arr[i][j])
        if cnt>=4:
            bomb_list.append(cnt)
        max_block = max(max_block,cnt)



print(len(bomb_list),max_block)
