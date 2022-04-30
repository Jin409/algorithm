"""
DP 를 안쓰고 풀었더니 오류 남. => Joy 가 더해지는 것을 고려 x 

"""
n = int(input())
L = list(map(int,input().split()))
J = list(map(int,input().split()))
L,J = [0]+L,[0]+J
dp = [[0 for _ in range(101)]for _ in range(n+1)]

#이전 사람과 악수해서 기쁨을 얻은 경우와 이전까지의 최댓값 중 더 큰 것을 넣는다. 
#dp[i][j] => i번째사람까지 악수하고 100-j만큼 체력이 있을 때의 기쁨의 최댓값
for i in range(1,n+1):
    for j in range(1,101):
        if L[i]<=j:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-L[i]]+J[i])
        else:
            dp[i][j] = dp[i-1][j]

#n번째 사람까지 악수하고, 체력이 1 남았을 때의 경우를 출력. 
print(dp[n][99])