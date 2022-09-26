n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    content = input()
    arr[i] = list(content)

result = 0

def check():
    global result
    for i in range(n):
        cnt = 1
        for j in range(1,n):
            if arr[i][j] == arr[i][j-1]:
                cnt +=1
            else:
                cnt = 1
            result = max(result, cnt)

        cnt = 1
        for j in range(1,n):
            if arr[j][i] == arr[j-1][i]:
                cnt +=1
            else:
                cnt = 1
            result = max(result, cnt)

# 색을 바꿨을 때 먹을 수 있는 사탕의 개수 구하기
# def find_result():

for i in range(n):
    for j in range(n):
        if j+1<n and arr[i][j]!=arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            check()
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

        if i+1<n and arr[i][j]!=arr[i+1][j]:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            check()
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

print(result)
