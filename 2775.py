t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    room = [0]*(n+1)
    for u in range(0,k+1):
        for j in range(1,n+1):
            if u==0:
                room[j]=j
            else:
                room[j]=room[j-1]+room[j]
    print(room[n])