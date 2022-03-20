#틀렸던 이유 : 증가를 고려하지 않음. 

n,m = map(int,input().split())
arr1 = [0]*1000000 #긱 인덱스는 시간!
arr2 = [0]*1000000

def move1(s,v,t):
    #s는 시작점 v는 속도 t는 시간
    idx = s
    for i in range(t):
        #이전에는
        #arr1[idx]=v 여서 틀림.
        arr1[idx]=arr1[idx-1]+v
        idx+=1
    return idx
    
now = 1

for i in range(n):
    v,t = map(int,input().split())
    now = move1(now,v,t)

def move2(s,v,t):
    #s는 시작점 v는 속도 t는 시간
    idx = s
    for i in range(t):
        arr2[idx]=arr2[idx-1]+v
        idx+=1
    return idx

now = 1

for i in range(m):
    v,t = map(int,input().split())
    now = move2(now,v,t)

cnt=0
first = 0

def check(i):
    global first
    if arr1[i]>arr2[i]:
        first = 1
    elif arr1[i]<arr2[i]:
        first = 2
    else:
        first = first
    return first



# print(arr1[1:now])
# print(arr2[1:now])

for i in range(1,now):
    temp_first = first
    if arr1[i]!=arr2[i]:
        first = check(i) 
        if temp_first!=0 and first!=temp_first:
            cnt+=1
    else:
        continue

print(cnt)

