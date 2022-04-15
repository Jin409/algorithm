n,k = map(int,input().split())

coin_arr = [
    int(input())
    for _ in range(n)
]


"""
k보다 크면 넘어가고, k보다 작으면
계속 단위별로 뺀다. 
-> 시간초과 났다
-> 
"""

coin_arr.sort(reverse=True)

cnt=0
idx=0

while k>0:
    if coin_arr[idx] > k:
        idx+=1
        continue
    elif k < coin_arr[idx]:
        idx+=1
    else:
        k -= coin_arr[idx]
        cnt+=1

print(cnt)