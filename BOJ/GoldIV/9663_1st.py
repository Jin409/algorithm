#-*- coding: utf-8 -*-

n = int(input()) 
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cnt = 0

# ������ �ִ��� Ȯ���ϴ� �Լ�
def in_range(x,y,n):
    return x<n and y<n and x>=0 and y>=0

# ���ǿ� �����ϴ��� Ȯ���ϴ� �Լ�
def condition(x,y,n):
    for i in range(n):
        for j in range(n):
            if i==x and j!=y and arr[i][j]==1:
                return False #���� �����ٿ� �̹� ü���� ���� ���̹Ƿ� False
            elif i!=x and j==y and arr[i][j]==1:
                return False #���� �����ٿ� �̹� ü���� ���� ���̹Ƿ� False
    
    idx_arr = []
    temp_x,temp_y = x,y
    
    #������ �Ʒ��� ���ϴ� �밢��
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

    #������ ���� ���ϴ� �밢��
    # (0,2) (1,1)
    
    while True:
        temp_x+=1
        temp_y-=1
        if not in_range(temp_x,temp_y,n):
            break
        idx_arr.append((temp_x,temp_y))
    
    # �밢�� ���ǿ� �ش��ϴ� �ε����� �˻��ϱ�
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
    
    # �̷��� �ϸ� Ž���ϰ� ���� �� ���� ĭ�� ��� Ž���ؾ� ���� �𸣰���
    arr[x][y]=1
    queen(x+1,y,n)
    queen(x+1,y+1,n)
    queen(x,y+1,n)
    arr[x][y]=0
    
    
    # �̷��� �ϸ� ��� �������� Ž���ؾ����� �𸣰���
    # for i in range(0,n):
    #     for j in range(0,n):
    #         arr[i][j]=1
    #         queen(i,j,n)
    #         arr[i][j]=0
   
queen(0,0,n)
print(cnt)