#-*- coding: utf-8 -*-

n = int(input()) 
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cnt = 0

# 범위에 있는지 확인하는 함수
def in_range(x,y,n):
    return x<n and y<n and x>=0 and y>=0

# 조건에 부합하는지 확인하는 함수
def condition(x,y,n):
    for i in range(n):
        for j in range(n):
            if i==x and j!=y and arr[i][j]==1:
                return False #같은 가로줄에 이미 체스가 놓인 것이므로 False
            elif i!=x and j==y and arr[i][j]==1:
                return False #같은 세로줄에 이미 체스가 놓인 것이므로 False
    
    idx_arr = []
    temp_x,temp_y = x,y
    
    #오른쪽 아래로 향하는 대각선
    while True:
        temp_x+=1
        temp_y+=1
        if not in_range(temp_x,temp_y,n):
            break
        idx_arr.append((temp_x,temp_y))
    
    temp_x,temp_y = x,y
    
    while True:
        temp_x-=1
        temp_y-=1
        if not in_range(temp_x,temp_y,n):
            break
        idx_arr.append((temp_x,temp_y))
    
    temp_x,temp_y = x,y

    #오른쪽 위로 향하는 대각선
    # (0,2) (1,1)
    
    while True:
        temp_x+=1
        temp_y-=1
        if not in_range(temp_x,temp_y,n):
            break
        idx_arr.append((temp_x,temp_y))
    
    # 대각선 조건에 해당하는 인덱스들 검사하기
    for idx in idx_arr:
        idx_x,idx_y = idx
        if arr[idx_x][idx_y]==1:
            return False
            
    return True
            
            
def queen(x,y,n):
    global cnt
    if not condition(x,y,n):
        return
    
    if x>=n:
        cnt+=1
        for i in range(n):
            for j in range(n):
                if arr[i][j]==1:
                    arr[i][j]=0 
        return
    
    if not in_range(x,y,n):
        return
    
    # 이렇게 하면 탐색하고 나서 그 다음 칸을 어떻게 탐색해야 할지 모르겠음
    arr[x][y]=1
    queen(x+1,y,n)
    queen(x+1,y+1,n)
    queen(x,y+1,n)
    arr[x][y]=0
    
    
    # 이렇게 하면 어떻게 다음줄을 탐색해야할지 모르겠음
    # for i in range(0,n):
    #     for j in range(0,n):
    #         arr[i][j]=1
    #         queen(i,j,n)
    #         arr[i][j]=0
   
queen(0,0,n)
print(cnt)