n,t = map(int,input().split())
r,c,d = input().split()
r,c = int(r)-1,int(c)-1

#n은 격자의 크기, t는 걸린 시간

#l과 r / u,d

dic_mapper = {
    #더하면 각각 합이 3
    "L":0,
    "U":1,
    "D":2,
    "R":3
}

def in_range(x,y):
    return x<n and y<n and x>=0 and y>=0

dxs = [0,-1,1,0]
dys = [-1,0,0,1]

dic_num = dic_mapper[d]

for i in range(t):
    #다음 위치
    nr = r+dxs[dic_num]
    nc = c+dys[dic_num]

    if not in_range(nr,nc):
        dic_num = 3-dic_num
    else: #범위에 들어있다면
        r,c = nr,nc

print(r+1,c+1)
