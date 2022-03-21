orders = list(input())

dxs = [0,1,0,-1]
dys = [1,0,-1,0]

# dic_map = {
#     "N":0,
#     "E":1,
#     "S":2,
#     "W":3
# }

x,y = 0,0
dic_num = 0

for order in orders:
    if order=="L":
        dic_num = (dic_num-1+4)%4
    elif order=="R":
        dic_num = (dic_num+1)%4
    else:
        x+=dxs[dic_num]
        y+=dys[dic_num]

print(x,y)