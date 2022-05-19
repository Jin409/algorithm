"""
계단은 한번에 한 / 두 계단씩 오를 수 있음
연속된 세개의 계단 밟으면 안됨
마지막 계단은 밟아야 됨
"""

n = int(input())
stairs = [
    int(input())
    for _ in range(n)
]

arr = [0]*n
arr[0] = stairs[0]
arr[1] = stairs[0]+stairs[1]
arr[2] = max(arr[0]+stairs[2],stairs[1]+stairs[2])

for i in range(3,n):
    arr[i] = max(arr[i-3]+stairs[i]+stairs[i-1],arr[i-2]+stairs[i])

print(arr[n-1])

# arr = [(0,0)]*n #각 계단에서의 점수를 계산
# arr[0] = (stairs[0],0)
# arr[1] = (arr[0][0]+stairs[1],1)

# for i in range(2,n-2):
#     if arr[i-1][1] == 1:
#         arr[i] = (arr[i-1][0],0)
#     else:
#         max_val = max(arr[i-1][1]+stairs[i],arr[i-1][1]+stairs[i+1])
#         if max_val == arr[i-1][1]+stairs[i]:
#             arr[i] = (max_val,1)
#         else:
#             arr[i] = arr[i-1]

#끝 부분에서 두가지 경우가 존재
#1. 15 10 20
#2. 25 20
#25를 거치면 15를 거쳤든 안거쳤든 두칸 뛰어야 함.




# print(arr[n-1][0]+stairs[n-1])