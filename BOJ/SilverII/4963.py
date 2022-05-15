"""
한 정사각형과 가로, 세로, 대각선으로 연결되어 있음 => 걸어갈 수 있는 사각형

"""

def recursive_dfs(v, arr,visited=[]):
    visited.append(v)
    for i in range(len(arr)):
        for j in range(len(arr[i]))
            if not w in visited:
                visited = recursive_dfs(w, visited)
    return visited


while True:
    w,h = map(int,input().split()) #너비, 높이
    if w==0 and h==0:
        break
    arr = [
        list(map(int,input().split()))
        for _ in range(h) #높이만큼 입력
    ]
    cnt=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]==1:
                recursive_dfs(arr[i][j],arr)
