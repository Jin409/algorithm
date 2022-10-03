from collections import deque

m,n,k = map(int,input().split())

arr = [
    [0 for _ in range(n)]
    for _ in range(m)
]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

for i in range(k):
    x1, y1, x2, y2 = map(int,input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            arr[j][k] = 1

def in_range(x,y):
    return x<m and y<n and y>=0 and x>=0

def bfs(x,y):
    result = 0
    q = deque([(x,y)])

    while q:
        x,y = q.popleft()
        if arr[x][y] != 1:
            arr[x][y]=1
            result +=1
            for i in range(4):
                nx = x+dxs[i]
                ny = y+dys[i]
                if in_range(nx,ny) and arr[nx][ny]==0:
                    q.append((nx,ny))
    return result

result_arr= []

for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            result_arr.append(bfs(i,j))

result_arr.sort()
print(len(result_arr))
for i in range(len(result_arr)):
    print(result_arr[i],end=' ')