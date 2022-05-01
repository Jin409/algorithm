"""
커서는 맨 앞, 맨 뒤, 중간 아무곳이나 위치 가능 
L 왼쪽으로 한칸, 이미 맨 앞이면 무시
D 오른쪽 한칸, 이미 맨 뒤면 무시 
B 왼쪽에 있는 문자 삭제 (맨 앞이면 무시) => 커서는 한칸 왼쪽으로 이동한\
    것처럼 보이지만 실제로 커서 오른쪽의 문자는 그대로!
P $ $라는 문자를 왼쪽에 추가하기 
"""

str_origin = list(input())
n = int(input())
order_list = [
    input()
    for _ in range(n)
]

#문자열의 각 문자 뒤에 커서의 공간 만들기 => 임의로 33으로 함!
#홀수번째에는 전부 문자가 위치하게 됨 
for i in range(1,len(str_origin)*2,2):
    str_origin.insert(i,33)
str_origin.insert(0,33)

cursor_idx = len(str_origin)-1 #초기 커서의 위치


for order in order_list:
    if order=="L":
        if cursor_idx==0:
            continue
        else:
            cursor_idx -=2
    elif order=="D":
        if cursor_idx==len(str_origin)-1:
            continue
        else:
            cursor_idx+=2
    elif order=="B":
        if cursor_idx==0:
            continue
        else:
            str_origin[cursor_idx-1]=33
    else:
        order_str = order[-1]
        if cursor_idx==0:
            str_origin.insert(0,order_str)
        else:
            str_origin.insert(cursor_idx,33)
            str_origin.insert(cursor_idx+1,order_str)
            cursor_idx +=2

for string in str_origin:
    if string!=33:
        print(string,end='')
