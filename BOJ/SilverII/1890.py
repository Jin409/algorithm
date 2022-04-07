# N*N 게임판. 0은 종착점. 오른쪽이나 아래로만 이동 가능. 
# 한번 점프 시에 방향을 바꿀 수는 없다 .
# 경로의 개수를 구하여라 

"""

완전탐색을 할까 했음 -> 너무 시간이 오래 걸릴 것 같음. 
재귀로 풀어봄 -> 시간초과가 뜸 (arr[x][y]==0 인 경우와
x==n-1 and y==n-1 인 경우에 return)
구글링으로 코드 참고해서 작성하기는 했는데 완벽하게 이해는 잘 안감..

"""

n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

dp = [
    [0]*n
    for _ in range(n) #방문횟수 저장 
]
dp[0][0]=1

for i in range(n):
    for j in range(n):
        if i==n-1 and j==n-1:
            break
        jmp_cnt = arr[i][j]

        x = i+jmp_cnt
        y = j+jmp_cnt

        if y<n:
            dp[i][y] += dp[i][j] #그 자리에 몇번 가는지 확인해보는듯..!
        if x<n:
            dp[x][j] += dp[i][j]

# for i in range(n):
#     for j in range(n):
#         print(dp[i][j],end='')
#     print()

print(dp[n-1][n-1])




# dxs = [0,1]
# dys = [1,0]
# cnt = 0 #경로의 개수를 센다

# def in_range(x,y):
#     return x<n and y<n and y>=0 and x>=0

# def move(x,y):
#     global cnt
#     if x==n-1 and y==n-1:
#         cnt+=1
#         return
#     elif arr[x][y]==0:
#         return
#     jump_cnt = arr[x][y] #점프할 수 있는 칸의 수
#     for i in range(2):
#         nx = x+(dxs[i]*jump_cnt)
#         ny = y+(dys[i]*jump_cnt)
#         if in_range(nx,ny):
#             move(nx,ny)



# move(0,0)
# print(cnt)


