# 2친구 구하기 -> 2친구가 되기 위해서는 두 사람이 친구이거나 두 사람과 친구인 제 3자가 존재해야 한다.

import sys
input = sys.stdin.readline

people_num = int(input())

"""
People_num이 너무 크면 input 에서 문제가 발생할 수 있기에 sys를 사용했다.
2친구를 알기 위해서는 두 경우가 존재한다.
1. 이미 나와 친구 2. 나와 친구는 아니지만 나와 친구인 사람과 친구
1번은 그냥 Y인 숫자를 세면 된다.
2번인 경우는 친구가 아닌 사람의 친구 정보와 나의 정보를 비교해보며 공통적으로 Y인 사람이 있는지 확인해보면 된다.
여기서 주의해야 할 것은 나 자신과는 친구가 아니라 N으로 표시되기에 이에서 제외시켜야 한다는 것이다.

"""

arr = []

for i in range(people_num):
    info = input()
    arr.append(info) #친구관계에 대한 정보 업데이트

#각 사람에 대하여 2친구를 구하고 최댓값을 반환한다.
max_num = 0

def calculate(person_num):
    info = arr[person_num]
    two_f_num = 0
    for i in range(len(info)):
        if info[i]=="Y":
            two_f_num +=1 #친구인 경우 우선 하나를 더한다. 
        elif info[i]=="N" and i!=person_num:#친구가 아니라면 연결되는 제3자가 있는지 확인
            not_friend = arr[i] #친구가 아닌 사람의 정보
            for j in range(len(arr[i])):
                if not_friend[j]=="Y" and info[j] =="Y":
                    two_f_num+=1
                    break
    return two_f_num

for i in range(people_num):
    two_f_num = calculate(i)
    max_num = max(max_num,two_f_num)

print(max_num)