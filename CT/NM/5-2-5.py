#n명의 개발자들 t번에 걸쳐서 악수
#k번의 악수에서만 전염성이 있음
#p 전염병에 걸린 사람
n,k,p,t = map(int,input().split())

arr = [0]*(n+1) #사람 배열
time_arr = [0]*251

arr[p]=1

for i in range(t):
    #x와 y가 악수를 나눈 시간
    time,x,y = map(int,input().split())
    time_arr[time]=tuple([x,y])

for i in range(len(time_arr)):
    if time_arr[i]!=0:
        #x와 y가 악수를 함.
        x,y = time_arr[i]
        #원래 감염자인 사람과 악수를 한 경우 => 어차피 감염자가 0보다 큰 숫자를 지님
        #감염을 시킬 때마다 1을 증가시키기 => 감염자인 경우(1)+횟수(k) 따라서 k+1 이 되면 더 이상 감염시키지 못하도록
        if (x>0 and x<(k+1)) or (y>0 and y<(k+1)):
            if (arr[x]==(k+1) and arr[y]==0) or (arr[y]==(k+1) and arr[x]==0):
                continue
            else:
                arr[x]+=1
                arr[y]+=1
            

#전염된 사람끼리 만나도 전염된 것으로 간주한다. 

for i in range(len(arr)):
    if arr[i]!=0:
        arr[i]=1

for i in range(1,len(arr)):
    print(arr[i],end='')

    