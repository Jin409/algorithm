'''
연속된 몇 개의 수를 선택해서 가장 큰 합 구하기
'''
import sys

input = sys.stdin.readline

n = int(input()) #수가 몇개인지
arr = list(map(int,input().split()))

dp = [0]*n #어디서부터 시작해서 하는지
dp[0] = arr[0]

for i in range(1,n):# 끝점
    # 연속할 것이냐, 끊을 것이냐
    dp[i] = max(dp[i-1]+arr[i],arr[i])
    
print(max(dp))

# 시간초과 났던 코드

# dp = [-sys.maxsize]*n #어디서부터 시작해서 하는지

# for i in range(1,n):# 끝점
#     hap = 0
#     for j in range(i): #0부터 나 이전까지만
#         # 이전까지 더했던 것들 + 지금 숫자 or 지금 숫자
#         hap = max(hap+arr[j],arr[j])
#     dp[i] = hap

