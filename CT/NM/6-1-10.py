n,m = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

cnt = 0

#시작점 정하기
for i in range(n-m+1):
    #해당 시작점부터 끝까지 
    if sorted(A[i:i+m])==sorted(B):
        cnt+=1

print(cnt)

n,k = map(int,input().split())
arr = [0]*101

#사탕의 개수와 바구니의 좌표
for i in range(n):
    loca,candy = map(int,input().split())
    arr[loca] = candy

#중심점 찾기
max_candy = 0
for i in range(k,101-k):
    result = 0
    for j in range(i-k,i+k+1):
        result += arr[j]
    max_candy = max(result,max_candy)

print(max_candy)
