# # # 자신의 위치에서 왼쪽 위, 대각선 왼쪽 아래, 대각선 오른쪽 아래로 움직일 수 있는 말이 비숍
# # # 서로 잡아먹지 않게 비숍 몇개를 놓을 수 있을지?

"""
완전탐색일 것 같다는 생각이 든다.
비숍이 놓인다면, 그 주위로 비숍이 이동할 수 없는 곳에 다음 비숍을 놓으면 된다.
-> 어이가 없음........짜증남........
그냥 규칙 찾아서 출력하는 문제였음!

"""

n = int(input())
if n<=2:
    print(n)
else:
    print(n+n-2)


# arr = [
#     [1]*n #이동 가능하다는 표시
#     for _ in range(n)
# ]



# #왼쪽 위는 -1 -1 오른쪽 아래는 +1 +1 왼쪽 아래는 +1 -1

# cnt = 0

# for i in range(n):
#     for j in range(n):
#         if arr[i][j]==1: 
#             arr[i][j]=2
#             cnt+=1
#             x,y = i,j
#             next_x = x-1
#             next_y = y-1
#             #범위 내에 있는 동안
#             while next_x >=0 and next_x < n and next_y >=0 and next_y < n:
#                 if arr[next_x][next_y] ==1:
#                     arr[next_x][next_y]=0 #놓을 수 없는 곳이라는 것을 표시
#                 next_x -=1
#                 next_y -=1
#             next_x = x-1
#             next_y = y+1
#             while next_x >=0 and next_x < n and next_y >=0 and next_y < n:
#                 if arr[next_x][next_y] ==1:
#                     arr[next_x][next_y]=0 #놓을 수 없는 곳이라는 것을 표시
#                 next_x -=1
#                 next_y +=1
#             next_x = x+1 
#             next_y = y+1
#             while next_x >=0 and next_x < n and next_y >=0 and next_y < n:
#                 if arr[next_x][next_y] ==1:
#                     arr[next_x][next_y]=0
#                 next_x += 1
#                 next_y += 1
#             next_x = x+1
#             next_y = y-1
#             while next_x >=0 and next_x < n and next_y >=0 and next_y < n:
#                 if arr[next_x][next_y] ==1:
#                     arr[next_x][next_y]=0
#                 next_x += 1
#                 next_y -= 1

# for i in range(n):
#     for j in range(n):
#         print(arr[i][j],end='')
#     print()

# print(cnt)

