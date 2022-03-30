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

