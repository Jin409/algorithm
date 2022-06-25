'''
고친 부분
1) 대각선 절댓값 이용해서 빼기
2) else
3) visited 로 방문한 열은 다시 방문하지 않기
'''

n = int(input())

arr = [0]*n
visited = [False]*n
cnt = 0

# 대각선
# 1,1 2,2 3,3 => arr[1]=1 arr[2]=2 arr[3]=3 이므로 뺐을 때의 절댓값이 같으면 x
# 0,2 1,1 => arr[0]=2 arr[1]=1 => 뺐을 때의 절댓값이 같음

def check(x):
    for i in range(x):
        if arr[i]==arr[x] or abs(arr[i]-arr[x])==abs(i-x):
            return False
    return True

def nqueens(x,n):
    global cnt 
    
    if x==n:
        cnt+=1
        return
    
    else:
        for i in range(n):
            if visited[i]==False:
                arr[x]=i
                if check(x):
                    visited[i]=True
                    nqueens(x+1,n)
                    visited[i]=False

nqueens(0,n)
print(cnt)
