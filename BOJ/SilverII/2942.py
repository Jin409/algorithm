# 빨간사과 R개 초록사과 G개 모든 선수에게 같은 개수 (남으면 안됨)
import math


r,g = map(int,input().split())



"""
약수 구하면 될 것 같음. 
-> 계속 시간 초과가 나는중..
최대공약수를 구할 때 루트만큼 시간이 걸리도록.
20 의 약수는
1 2 4 5 10 20 -> 대칭적인 형상을 띄기 때문에 루트 20인 4를 이용하여 계산
"""

#최대공약수 반환
def find_num(num):
    num_list = []
    sqrt_num = int(math.sqrt(num))
    for i in range(1,sqrt_num+1):
        if num%i==0:
            num_list.append(i)
            if num//i == i and i!=1:
                continue 
            else:
                num_list.append(num//i)
    return num_list


min_num = min(r,g)
c_list = find_num(min_num) #공약수 리스트
num_list = find_num(max(c_list))

for i in range(len(num_list)):
    num = num_list[i]
    if r%num==0 and g%num==0:
        print(f"{num_list[i]} {r//num_list[i]} {g//num_list[i]}")

