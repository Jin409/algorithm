import sys
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

result_arr = []

def get_arr(result,i,cnt):
    if cnt==m:
        result = result.lstrip()
        if not result in result_arr:
            result_arr.append(result)
        return
    if i==len(arr):
        return
    get_arr(result,i+1,cnt) #더하지 않고
    get_arr(result+str(arr[i]),i+1,cnt+1) #더하고

get_arr("",0,0)

#거꾸로 더하기
for i in range(len(result_arr)):
    reversed_result = result_arr[i][::-1]
    if reversed_result not in result_arr:
        result_arr.append(reversed_result)

for i in range(len(result_arr)):
    result_arr[i] = list(result_arr[i])
    for j in range(len(result_arr[i])):
        result_arr[i][j] = int(result_arr[i][j])

result_arr.sort()

for i in range(len(result_arr)):
    for j in range(len(result_arr[i])):
        print(result_arr[i][j],end=' ')
    print()