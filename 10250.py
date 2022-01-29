k = int(input())

for i in range(k):
    h, w, n = map(int, input().split())
    y = n//h+1
    x = n%h
    if x==0:
        x = h
        y = n//h
    print(f'{x*100+y}')
    