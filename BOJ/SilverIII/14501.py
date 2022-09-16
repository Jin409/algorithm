n = int(input()) #n+1 일차에 퇴사할 것.
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]
arr.insert(0,0)

dp = [0 for _ in range(n+1)]

for i in range(n-1, 0, -1):
    # 지금을 선택안하는 경우 -> 이전 dp 의 값을 가져옴
    if i + arr[i][1] > n:
        dp[i] = dp[i+1]

    # 지금을 선택하는 경우 -> 이전 dp의 값과 (지금 값 + 이전 dp의 값을 더한 것) 중 큰 값으로
    else:
        dp[i] = max(dp[i+1], arr[i][1] + dp[i + arr[i][0]])
