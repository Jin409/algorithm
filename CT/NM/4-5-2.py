# 세번째 입력된 직사각형으로 덮이지 않은 넓이의 합 

arr = [
    [0 for _ in range(2001)]
    for _ in range(2001)
]

# 직사각형 a, b 를 배열에 표시하기
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
            arr[i][j]=1

def check_m(x1,y1,x2,y2):
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
            arr[i][j]=3


for i in range(3):
    x1,y1,x2,y2 = map(int,input().split())
    if i==2:
        check_m(x1,y1,x2,y2)
    else:
        check(x1,y1,x2,y2)

count=0

for i in range(2001):
    for j in range(2001):
        if arr[i][j]==1:
            count+=1

print(count)