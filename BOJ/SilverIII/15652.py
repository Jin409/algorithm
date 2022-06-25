n,m = map(int,input().split()) #n은 제한 / m은 길이

ans = []

def dfs():
    if len(ans)==m:
        print(*ans)
        return
    
    for i in range(1,n+1):
        if len(ans)==0 or len(ans)>=1 and ans[-1]<=i:
            ans.append(i)
            dfs()
            ans.pop()

dfs()