# 빨간사과 R개 초록사과 G개 모든 선수에게 같은 개수 (남으면 안됨)
import math


r,g = map(int,input().split())

n = 0

"""
약수 구하면 될 것 같음. 
-> 계속 시간 초과가 나는중..

"""

c_list =[]

min_num = min(r,g)
min_num = int(math.sqrt(min_num))


for i in range(1,min_num+1):
    if g%i==0 and r%i==0:
        c_list.append(i)

c_list[-1]

for i in range(len(c_list)):
    print(f"{c_list[i]} {r//c_list[i]} {g//c_list[i]}")

