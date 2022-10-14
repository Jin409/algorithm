n, c, w = map(int,input().split()) #나무의 길이, 자르는데에 드는 가격, 한 단위의 가격

arr = [
    int(input())
    for _ in range(n)
]

result = 0

for i in range(1, max(arr)+1):
    earn = 0
    for j in range(n):
        cnt = arr[j]//i
        cost = 0
        if arr[j]%i==0:
            cost = (cnt-1)*c
        else:
            cost = cnt*c
        money = (w * cnt * i)-cost
        if money < 0:
            continue
        earn += money
    result = max(earn, result)


print(result)