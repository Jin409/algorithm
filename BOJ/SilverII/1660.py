# 부모와 자식 사이 1촌
# 아버지 - 아버지 형제 2촌
# -> 아버지와 나 1촌 + 아버지 아버지 형제 2촌 => 3촌!

from shlex import join


n = int(input()) #사람 수
arr = [0]*(n+1) #0번째 인덱스는 안쓸것!

p1, p2 = map(int,input().split()) #p1 p2 간의 촌수 계산

m = int(input())

for i in range(m):
    x,y = map(int,input().split())
    arr[y] = x #부모의 인덱스 저장하기
    # 각 인덱스에는 부모의 정보가 저장되어 있음
    # 부모의 정보가 없는 경우는 0으로 저장되어 있음.




#촌수 세기
def cnt(p1,p2):
    arr_1 = [] 
    arr_2 = []
    common = [] #공통인 숫자를 넣기
    #거슬러올라가면서 자신의 조상들을 전부 넣기
    #같은 숫자나 p1, p2 가 있으면 관계 있음

    i,j = p1,p2
    while arr[i]!=0 and arr[j]!=0:
        arr_1.append(arr[i])
        arr_2.append(arr[j])
        i,j = arr[i],arr[j]
    while arr[i]!=0:
        arr_1.append(arr[i])
        i = arr[i]
    while arr[j]!=0:
        arr_2.append(arr[j])
        j = arr[join]

    is_it_related = False

    if p1 in arr_2:
        is_it_related = True
    elif p2 in arr_1:
        is_it_related = True
    else: #p1, p2 가 둘 다 없다면
        for i in range(len(arr_1)):
            if arr_1[i] in arr_2:
                common.append(arr_1[i])
                is_it_related = True
        for i in range(len(arr_2)):
            if arr_2[i] in arr_1 and arr_2[i] not in common:
                common.append(arr_2[i])
                is_it_related = True
    if not is_it_related:
        return -1
    cnt=0
    
    return len(arr_1)+len(arr_2)



    #겹치는 부모 세기
    
    

    
print(cnt(p1,p2))














