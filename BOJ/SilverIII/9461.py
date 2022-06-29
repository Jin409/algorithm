t = int(input()) #테스트케이스의 개수

dp = [0,1,1,1,2,2,3,4,5,7,9]
# 직전의 변 + 11일떄 3 (6)
dp.extend([0]*90)

def solution(n):
    if dp[n]:
        return dp[n]
    for i in range(11,n+1):
        dp[i] = dp[i-1]+dp[i-5]
    return dp[n]

for _ in range(t):
    print(solution(int(input())))