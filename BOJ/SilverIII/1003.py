t = int(input())

# 0이 몇번 등장하는지


for _ in range(t):
    n = int(input())
    dp = [0 for _ in range(41)]
    dp[0] = [1,0]
    dp[1] = [0,1]

    for i in range(2,n+1):
        dp[i] = [dp[i-1][0]+dp[i-2][0],dp[i-1][1]+dp[i-2][1]]

    print(f"{dp[n][0]} {dp[n][1]}")