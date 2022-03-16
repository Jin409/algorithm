#사각형의 넓이 구하기, 겹쳐질 수도 있음.

n = int(input())

arr = [
    [0 for _ in range(201)]
    for _ in range(201)
]

#해당 사각형 부분에 전부!
def check(x1,y1,x2,y2):
    if x1<x2:
        start_x_point = x1
        end_x_point = x2
    else:
        start_x_point = x2
        end_x_point = x1

    if y1<y2:
        start_y_point = y1
        end_y_point = y2

    else:
        start_y_point = y2
        end_y_point = y1

    for i in range(start_x_point,end_x_point):
        for j in range(start_y_point,end_y_point):
            arr[i][j]+=1

for i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    check(x1,y1,x2,y2)

count = 0

for i in range(201):
    for j in range(201):
        if arr[i][j]:
            count+=1

print(count)
