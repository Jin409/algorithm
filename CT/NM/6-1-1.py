n = int(input())
people = list(map(int,input().split()))
result = []

for i in range(n):
    #집 옮기기
    cnt=0
    for j in range(n):
        cnt+=people[j]*(abs(i-j))
    result.append(cnt)

print(min(result))