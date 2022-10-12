import sys

n = int(input())
arr = list(map(int,input().split()))
a, b = map(int,input().split()) # a 에서 시작해서 b로
a, b = a-1, b-1
result = sys.maxsize

def sol(now,cnt=0):
    global result

    if now >= len(arr) or now>=b:
        return -1

    if now == b:
        return cnt

    jump = arr[now]
    idx = 1
    while True:
        new_idx = now+jump*idx
        if new_idx >= len(arr):
            return cnt
        if result != -1 :
            result = min(sol(new_idx,cnt+1), result)
        idx+=1

sol(a)
print(result)
