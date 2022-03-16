n = int(input())

arr = [
    [0 for _ in range(201)]
    for _ in range(201)
]

def check(x,y):
    for i in range(x,x+8):
        for j in range(y,y+8):
            arr[i][j]=1

for i in range(n):
    x,y = map(int,input().split())
    check(x,y)

count=0

for i in range(201):
    for j in range(201):
        if arr[i][j]:
            count+=1

print(count)