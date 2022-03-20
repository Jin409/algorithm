n,m = map(int,input().split())

arr_1 = [0]*10000000 #로봇 A의 시간별 위치
arr_2 = [0]*10000000 #로봇 B의 시간별 위치

a_time = 1

for i in range(n):
    #시간과 방향 / 방향은 왼,오만 있음.
    t,d = input().split()
    t = int(t)
    if d=="L":
        dir_num = -1
    else:
        dir_num = 1
    for j in range(t):
        arr_1[a_time] = arr_1[a_time-1]+dir_num #이전 위치에서 dir_num만큼 더한다. 만약 이전 위치가 3이고 왼쪽으로 1칸이면 3 - 1 = 2 가 된다.
        a_time+=1

b_time = 1

for i in range(m):
    #시간과 방향 / 방향은 왼,오만 있음.
    t,d = input().split()
    t = int(t)
    if d=="L":
        dir_num = -1
    else:
        dir_num = 1
    for j in range(t):
        arr_2[b_time] = arr_2[b_time-1]+dir_num #이전 위치에서 dir_num만큼 더한다. 만약 이전 위치가 3이고 왼쪽으로 1칸이면 3 - 1 = 2 가 된다.
        b_time+=1

if a_time < b_time:
    min_time = a_time
    max_time = b_time
    max_arr = arr_2
    min_arr = arr_1
else:
    min_time = b_time
    max_time = a_time
    max_arr = arr_1
    min_arr = arr_2

cnt=0

# 두 시간이 겹치는 지점까지는 우선 for 문을 사용하기
for i in range(2,min_time):
    if arr_1[i-1]!=arr_2[i-1] and arr_1[i]==arr_2[i]:
        cnt+=1

#arr는 아직 다 못 돈 배열
for i in range(min_time,max_time):
    if min_arr[min_time-1]!=max_arr[i-1] and max_arr[i]==min_arr[min_time-1]:
        cnt+=1

print(cnt)
