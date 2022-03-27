n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return x<n and y<n and x>=0 and y>=0

max_cnt = 0

#꼭짓점 잡기
for i in range(n):
    for j in range(n-2):
        cnt = arr[i][j]+arr[i][j+1]+arr[i][j+2]
        max_cnt = max(cnt,max_cnt)

print(max_cnt)
    
