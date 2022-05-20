"""
"""

n = int(input())
arr = list(map(int,input().split()))
new_arr = [[0,0,0]]*n
#이전 값, 새로운 값, 이전 인덱스 값

for i in range(n):
    new_arr[i] = [arr[i],0,i]

new_arr.sort()

for i in range(1,n):
    old_value = new_arr[i][0]
    new_value= new_arr[i][1]
    origin_idx = new_arr[i][2]
    #이전값과 같을 경우
    if old_value == new_arr[i-1][0]:
        new_arr[i][1] = new_arr[i-1][1]
    else:
        new_arr[i][1] = new_arr[i-1][1]+1

result_arr = [0]*n

for i in range(len(new_arr)):
    result_arr[new_arr[i][2]] = new_arr[i][1]

for i in range(len(result_arr)):
    print(result_arr[i],end=' ')

# result_arr = [0]*n

# #나보다 작은게 몇개인지만 알면!
# for i in range(len(arr)):
#     cnt=0
#     for j in range(len(arr)):
#         if i==j:
#             continue
#         if arr[i]>arr[j]:
#             cnt+=1
#     result_arr[i] = cnt

# set_result_arr = list(set(result_arr))
# set_result_arr.sort()
# num_dict = {}

# cnt=0
# for i in range(len(set_result_arr)):
#     num_dict[set_result_arr[i]] = cnt
#     cnt+=1

# for i in range(len(result_arr)):
#     num = num_dict.get(result_arr[i])
#     result_arr[i] = num

# for i in range(len(result_arr)):
#     print(result_arr[i],end=' ')