n,l,w,h = map(int,input().split())

start, end = 0, min(l,w,h)

for _ in range(100):
    middle = (start+end)/2
    if (l//middle)*(w//middle)*(h//middle) >= n:
        start = middle
    else:
        end = middle

print(f"%.10f"%(end))