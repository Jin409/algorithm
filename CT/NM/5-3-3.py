n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

dxs = [-1,1,0,0]
dys = [0,0,-1,1]



def in_range(x,y):
    return x<n and y<n and x>=0 and y>=0

result_cnt=0

def count(x,y):
    cnt=0
    for i in range(4):
        nx=x+dxs[i]
        ny=y+dys[i]
        if in_range(nx,ny) and arr[nx][ny]==1:
            cnt+=1
    if cnt>=3:
        return True
    else:
        return False


for i in range(n):
    for j in range(n):
        if count(i,j):
            result_cnt+=1

print(result_cnt)
        