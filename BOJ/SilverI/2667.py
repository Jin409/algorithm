# 1은 집이 있는 곳, 0은 집이 없는 곳
# 연결된 집은 단지 => 단지에 번호를 붙이기
# 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하기

n = int(input()) #가로, 세로의 길이

arr = [
    list(map(int,input()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

houses = []

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x,y,n):
    return x<n and y<n and x>=0 and y>=0

def dfs(x,y,arr,visited,n):
    global cnt

    if not in_range(x,y,n) or visited[x][y]:
        return False

    visited[x][y]=True

    if arr[x][y]==1:
        cnt+=1
        for i in range(4):
            nx = x+dxs[i]
            ny = y+dys[i]
            # if in_range(nx,ny,n) and not visited[nx][ny]:
            dfs(nx, ny,arr,visited,n)
        return True
    return False


for i in range(n):
    for j in range(n):
        if dfs(i,j,arr,visited,n) == True:
            houses.append(cnt)
            cnt = 0

print(len(houses))
for i in range(len(houses)):
    print(houses[i])