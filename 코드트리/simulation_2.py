n,m,k = map(int,input().split())
k-=1
#n = 격자의 크기 / m = 블록의 크기 / k = k~k+m-1 까지 차지함
arr = []
for i in range(n):
    num = list(map(int,input().split()))
    arr.append(num)

def all_blank(row,col_s,col_e):
    for i in range(col_s,col_e+1):
        if arr[row][i]:
            return False
    return True

def target_row():
    for row in range(n-1):
        #다음 줄이 블랭크가 아니라면 거기서 멈춰야 하므로
        if not all_blank(row+1,k,k+m-1):
            return row
    #모두 블랭크일 경우에는 
    return 0

target_row = target_row()

for col in range(k, k + m):
    arr[target_row][col] = 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()