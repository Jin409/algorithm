'''
1. x가 3으로 나눠떨어지면 3으로 나누기
2. 2로 나눠떨어지면 2로 나누기
3. 1을 빼기
'''

n = int(input())
dp = [0]*(n+1)

# def solution(n,cnt):
#     if dp[n]!=sys.maxsize:
#         return dp[n]
    
#     if n%2==0:
#         cnt +=1
#         dp[n] = min(solution(n-1,0),solution(n//2,0))+cnt
#     elif n%3==0:
#         cnt +=1
#         dp[n] = min(solution(n-1,0),solution(n//3,0))+cnt
#     else:
#         cnt+=1
#         dp[n] = solution(n-1,0)+cnt

#     return dp[n]


if n==1:
    print(0)
elif n==2:
    print(1)
else:
    dp[2] = 1
    
    for i in range(3,n+1):
        dp[i] = dp[i-1]+1 #1 빼는 것
        
        if i%2==0: #2로 나누는 것
            dp[i] = min(dp[i],dp[i//2]+1)
            
        if i%3==0:
            dp[i] = min(dp[i],dp[i//3]+1)

    print(dp[n])