n = int(input()) #동기의 수
m = int(input()) #리스트의 길이

arr = [
    []
    for _ in range(n+1)
]

for i in range(m):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

result = []

for i in range(len(arr[1])):
    now = arr[1][i]
    if not now in result and now!=1:
        result.append(now) #지금 보고 있는 친구
    for j in range(len(arr[now])):
        if not arr[now][j] in result and arr[now][j]!=1:
            result.append(arr[now][j])

print(len(result))
