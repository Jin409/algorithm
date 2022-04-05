import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

"""

깊이우선 탐색으로 구역이 얼마나 되는지 세어봐야 한다.
재귀를 할 때에는
import sys
sys.setrecursionlimit(10 ** 6) 로 파이썬의 재귀 제한을 높여주어야 한다.
input = sys.stdin.readline 으로 입력 받아야 여러 줄을 입력 받는 경우에 시간초과가 발생하지 않는다. 

"""

t = int(input()) #테스트케이스의 개수

#상하좌우를 탐색하기 위해서
def search(x,y):
    if x >= n or y>=m or y <0 or x < 0:
        return
    
    if arr[x][y]==0:
        return

    #위의 조건에 모두 해당되지 않고 방문한 곳은 0으로

    arr[x][y] = 0

    search(x-1,y) #상
    search(x+1,y) #하
    search(x,y-1) #좌
    search(x,y+1) #우
    


# 테스트케이스만큼 반복
for i in range(t):
    global arr

    m,n,k = map(int,input().split())

    arr = [
        [0]*(m)
        for _ in range(n)
        ]

    for j in range(k):
        y,x = map(int,input().split())
        arr[x][y] = 1 #배추가 있다고 표시 
    
    start_x = 0
    start_y = 0
    cnt = 0

    for j in range(n):
        for k in range(m):
            if arr[j][k]==1: #배추가 심어진 경우, search를 부른다.
                search(j,k)
                cnt+=1
    
    print(cnt)


    




