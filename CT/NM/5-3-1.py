n = int(input())

nxs = [-1,1,0,0]
nys = [0,0,-1,1]

dic_map = {
    "W":0,
    "E":1,
    "S":2,
    "N":3
}

x,y=0,0

for i in range(n):
    dic,dis = input().split()
    dis = int(dis)
    dic_num = dic_map[dic]
    for i in range(dis):
        x+=nxs[dic_num]
        y+=nys[dic_num]

print(x,y)

        