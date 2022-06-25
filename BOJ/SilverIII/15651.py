n,m = map(int,input().split()) #n은 limmit, m은 길이

ans = []

def dfs():
    if len(ans)==m:
        print(*ans)
        return
    
    for i in range(1,n+1):
        ans.append(i)
        dfs()
        ans.pop()
        
dfs()