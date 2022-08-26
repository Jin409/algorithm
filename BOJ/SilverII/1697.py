# x일 때 걸으면 x-1 / x+1
# 순간이동을 하면 2x 의 위치로 이동

import sys
from collections import deque

n,k = map(int,input().split()) #n은 수빈이의 / k 는 동생의 위치

min_value = sys.maxsize
max_size = 100000

arr = [
    0 for _ in range(max_size+1)
]

def in_range(x):
    return x>=0 and x<=max_size

def dfs(x,k):
    q = deque([x])

    while q:
        now = q.popleft()
        if now == k:
            break

        if in_range(now-1) and arr[now-1]==0:
            arr[now-1] = arr[now]+1
            q.append(now-1)

        if in_range(now+1) and arr[now+1]==0:
            arr[now+1] = arr[now]+1
            q.append(now+1)

        if in_range(now*2) and arr[now*2]==0:
            arr[2*now] = arr[now]+1
            q.append(now*2)

dfs(n,k)
print(arr[k])