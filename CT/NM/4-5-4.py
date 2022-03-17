import sys

arr = [
    [0 for _ in range(2000)]
    for _ in range(2000)
]

def check(x1,y1,x2,y2,num):
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
            arr[i][j]=num

#잔해물은 arr에서 1로 표시됨!
for i in range(2):
    x1,y1,x2,y2 = map(int,input().split())
    check(x1+1000,y1+1000,x2+1000,y2+1000,i+1)

min_x = sys.maxsize
max_x = -sys.maxsize

min_y = sys.maxsize
max_y = -sys.maxsize

for i in range(2000):
    for j in range(2000):
        if arr[i][j]==1:
            if min_x>i:
                min_x = i
            elif max_x<i:
                max_x = i

            if min_y>j:
                min_y = j
            elif max_y<j:
                max_y = j

result = ((max_x+1) - min_x) * ((max_y+1) - min_y)
print(result)

