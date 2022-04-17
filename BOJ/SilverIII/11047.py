n,k = map(int,input().split())

coin_arr = [
    int(input())
    for _ in range(n)
]

"""
k보다 크면 넘어가고, k보다 작으면
계속 단위별로 뺀다. 
-> 시간초과 났다
-> while 문을 어떻게 하면 안 쓸 수 있을지 고민.. 
"""

cnt=0

coin_arr.sort(reverse=True)

for coin in coin_arr:
    if k<=0:
        break
    elif coin > k:
        continue
    cnt+=k//coin
    k %=coin
    
print(cnt)