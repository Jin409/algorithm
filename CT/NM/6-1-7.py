n = int(input())
dis = [0]*n
copy_dis = [0]*n

for i in range(n):
    dis[i] = tuple(map(int,input().split()))
    copy_dis[i] = dis[i]

result = []

def copy():
    global copy_dis
    copy_dis = []
    for i in range(len(dis)):
        copy_dis.append(dis[i])

def count():
    result_num = 0
    for i in range(1,len(copy_dis)):
        x1,y1 = copy_dis[i-1]
        x2,y2 = copy_dis[i]
        result_num += (abs(x1-x2)+abs(y1-y2))
    result.append(result_num)

for i in range(1,n-1):
    del copy_dis[i]
    count()
    copy()

print(min(result))