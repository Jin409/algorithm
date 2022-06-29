n = int(input()) #구하고자 하는 숫자
arr = [0,0]
dp = [0]*(n+1)

def code_1(n):
    if n==1 or n==2:
        return 1
    arr[0]+=1
    return code_1(n-1)+code_1(n-2)
    
def code_2(n):
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        arr[1]+=1
        dp[i] = dp[i-1]+dp[i-2]

code_1(n)
code_2(n)
print(arr[0]+1,end=' ')
print(arr[1])
