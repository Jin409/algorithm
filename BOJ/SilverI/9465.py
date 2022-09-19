t = int(input())

#테스트케이스
for _ in range(t):
    n = int(input())
    stickers = [
        list(map(int,input().split()))
        for _ in range(2)
    ]

    for j in range(1,n):
        if j==1:
            stickers[0][j] = stickers[0][j]+stickers[1][j-1]
            stickers[1][j] = stickers[1][j]+stickers[0][j-1]
        else:
            stickers[0][j] = max(stickers[1][j-1], stickers[1][j-2])+stickers[0][j]
            stickers[1][j] = max(stickers[0][j-1], stickers[0][j-2])+stickers[1][j]


    print(max(map(max,stickers)))
