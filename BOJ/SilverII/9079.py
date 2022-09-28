t = int(input())

def change(x, y):
    if arr[x][y] == "H":
        arr[x][y] = "T"
    else:
        arr[x][y] = "H"

def check():
    origin_val = arr[0][0]
    for i in range(3):
        for j in range(3):
            if arr[i][j] != origin_val:
                return False
    return True

for _ in range(t):
    arr = [
        list(map(input().split()))
        for _ in range(3)
    ]

    result = 0

    


