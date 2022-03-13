import math
a,b,v = map(int,input().split())
day = (v-b)/(a-b)
print(math.ceil(day))

#시간초과로 오답
# a,b,v = map(int,input().split())
# day = 0
# while v>=0:
#     day+=1
#     v=v-a
#     if v<=0:
#         break
#     v=v+b
# print(day)
