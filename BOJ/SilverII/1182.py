# 합이 s가 되는 부분수열의 개수 출력
n, s = map(int,input().split())
arr = list(map(int,input().split()))

ans = 0

def sol(idx, result):
    global ans

    if idx >= n:
        return

    result += arr[idx]

    if result == s:
        ans+=1

    sol(idx+1,result)
    sol(idx+1, result-arr[idx])

sol(0,0)
print(ans)