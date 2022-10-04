import sys
sys.setrecursionlimit(2500)

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

arr = [
    list(map(int,input().split()))
    for _ in range(5)
]

result = []

def in_range(x,y):
    return x<5 and y<5 and x>=0 and y>=0

def move(x,y, num=""):
    if len(num) == 6:
        result.append(num)
        return
    for i in range(4):
        nx = x+dxs[i]
        ny = y+dys[i]
        if in_range(nx,ny):
            move(nx,ny,num+str(arr[nx][ny]))

for i in range(5):
    for j in range(5):
        move(i,j,str(arr[i][j]))

print(len(set(result)))
