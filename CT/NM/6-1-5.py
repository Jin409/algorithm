r,c = map(int,input().split()) #r은 세로, c는 가로

arr = [
    list(input().split())
    for _ in range(r)
]

#색이 다른 곳으로만 점프가 가능하다.
#점프시에는 적어도 한칸 오른쪽 / 한칸 이상 아래에 있어야 한다.
#시작, 도착 이외에는 도달하는 위치가 2곳뿐이어야 한다.

start_x,start_y = 0, 0
cnt = 0

for i in range(1,r):
    for j in range(1,c):
        for k in range(i+1,r-1):
            for l in range(j+1,c-1):
                if arr[0][0]!=arr[i][j] and arr[i][j]!=arr[k][l] and arr[k][l]!=arr[r-1][c-1]:
                    cnt+=1

print(cnt)

        