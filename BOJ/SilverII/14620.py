import sys

n = int(input()) #화단 한 변의 길이
arr = [
    list(map(int,input().split()))
    for _ in range(n)
] #True라면 이미 방문했다는 의미
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
answer = sys.maxsize

def in_range(x,y):
    return x>=0 and y>=0 and x<n and y<n

def cnt_center(center): #센터가 가능한 위치인지 아닌지 + 해당을 센터로 썼을 때의 cost 가 얼마인지
    x,y = center
    move_arr = [center] #어디어디를 방문하는지
    move_dir = [(-1,0),(1,0),(0,1),(0,-1)]
    for i in range(len(move_dir)):
        new_x, new_y = x+move_dir[i][0], y+move_dir[i][1]
        if not in_range(new_x, new_y) or visited[new_x][new_y] == True:
            return False
        move_arr.append((new_x, new_y))
    return move_arr

# 센터 3개를 어떻게 잡지..?

def find_answer(x,y,cost,cnt):
    global answer
    if cnt==3:
        answer = min(answer, cost)
        return
    for i in range(x,n):
        for j in range(n):
            if x==i and y==j:
                continue
            result_arr = cnt_center((i,j))
            if not result_arr:
                continue
            temp_cost = 0
            for idx in result_arr:
                idx_x, idx_y = idx
                temp_cost += arr[idx_x][idx_y]
                visited[idx_x][idx_y] = True
            find_answer(i,j,cost+temp_cost,cnt+1)
            for idx in result_arr:
                idx_x, idx_y = idx
                visited[idx_x][idx_y] = False

find_answer(0,0,0,0)
print(answer)
