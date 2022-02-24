from collections import deque

n,k,u,d = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

select_city = [
    [0 for _ in range(n)]
    for _ in range(n)
]

dxs = [0,0,-1,1]
dys = [-1,1,0,0]

q = deque()

############################################################

#can_go 함수에 조건 하나 더 추가하기 u,d

def in_range(x,y):
    return x<n and y<n and x>=0 and y>=0

def can_go(x,y,height):
    if not in_range(x,y):
        return False

    if visited[x][y]:
        return False

    if abs(height-arr[x][y])>d or abs(height-arr[x][y])<u:
        return False

    return True
    
def bfs():
    while q:
        x,y = q.popleft()
        height = arr[x][y]

        #왼오오상상하
        for dx,dy in zip(dxs,dys):
            nx = dx+x
            ny = dy+y
            if can_go(nx,ny,height):
                visited[nx][ny]=1
                q.append((nx,ny))

def calc():

    cnt = 0

    for i in range(n):
        for j in range(n):
            if select_city[i][j]:
                x,y = i,j
                q.append((x,y))
                visited[x][y] = 1
    
    bfs()

    for i in range(n):
        for j in range(n):
            if visited[i][j]==1:
                cnt+=1

    for i in range(n):
        for j in range(n):
            visited[i][j]=0
    
    return cnt

max_cnt = 0

#위치 튜플로 받아서 저장하기
def choose(cnt):
    global max_cnt

    if cnt==k:
        # for i in range(n):
        #     print(select_city[i])
        # print("+++")
        max_cnt = max(max_cnt,calc())
        return

    for i in range(n):
        for j in range(n):
            if select_city[i][j]==0:
                select_city[i][j]=1
                choose(cnt+1)
                select_city[i][j]=0

choose(0)
print(max_cnt)

