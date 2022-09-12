import sys

input = sys.stdin.readline

n,m = map(int,input().split())

arr = [
    int(input())
    for _ in range(n)
]
arr.sort()
ans = 0

def cnt(mid, m):
    sum = 0
    cnt = 0
    if mid < max(arr):
        return False

    for i in range(n):
        if sum - arr[i]<0:
            sum = mid
            cnt +=1
        sum -= arr[i]
    return m >= cnt

def binary_search(m, start, end):
    global ans

    if start > end:
        return

    mid = (start+end)//2
    result = cnt(mid, m)

    # 횟수가 타겟보다 더 작으니까 맞는 경우
    if result:
        ans = mid
        return binary_search(m, start, mid-1)
    else:
        return binary_search(m, mid+1, end)

binary_search(m, min(arr), sum(arr))
print(ans)
