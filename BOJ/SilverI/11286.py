"""
배열에 정수를 넣음 => 절댓값이 가장 작은 값 출력 / 해당 배열에서 제거
절댓값이 가장 작은 값이 여러개인 경우에는 가장 작은 수 출력, 배열에서 제거

1.숫자를 넣어야 하는 경우에 더 작은수가 앞으로 가도록 해야 함.
"""

from collections import deque

dq = deque([])
n = int(input())

for _ in range(n):
    order = int(input())
    if order!=0: #숫자를 넣어야 하는 경우
        if len(dq)==0:
            dq.append(order)
        else:
            num = dq.popleft() #맨앞에 있는 수를 팝
            if abs(num) == abs(order): #절댓값이 같다면 -1, 1
                if num < order: #새로 넣으려는 수가 더 큼
                    cnt = 1
                    while len(dq)>0:
                        num_2 = dq.popleft()
                        if num == dq.popleft():
                            cnt+=1
                        else:
                            dq.appendleft(num_2)
                            break
                    dq.appendleft(order)
                    for _ in range(cnt):
                        dq.appendleft(num)
                else:
                    dq.appendleft(num)
                    dq.appendleft(order)
            elif abs(num) > abs(order):
                dq.appendleft(num)
                dq.appendleft(order)
            else: #기존에 있는 숫자가 더 작을경우
                while len(dq)>0:
                    







# for _ in range(n):
#     order = int(input())
#     if order==0:
#         if len(dq)==0:
#             print(0)
#         elif len(dq)==1:
#             print(dq.popleft())
#         else:
#             num = dq.popleft()
#             num_2 = dq.popleft()
#             if abs(num) == abs(num_2):
#                 min_num = min(num,num_2)
#                 max_num = max(num,num_2)
#                 print(min_num)
#                 dq.appendleft(max_num)
#             else:
#                 print(num)
#                 dq.appendleft(num_2)
#     else:
#         if len(dq)==0:
#             dq.appendleft(order)
#         else:
#             num = dq.pop()
#             if  abs(num) > abs(order):
#                 dq.append(num)
#                 dq.appendleft(order)
#             elif abs(num)==abs(order):
#                 if num < order:

#             else:
#                 dq.append(num)
#                 dq.append(order)
