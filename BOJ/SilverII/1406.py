"""
커서는 맨 앞, 맨 뒤, 중간 아무곳이나 위치 가능
L 왼쪽으로 한칸, 이미 맨 앞이면 무시
D 오른쪽 한칸, 이미 맨 뒤면 무시
B 왼쪽에 있는 문자 삭제 (맨 앞이면 무시) => 커서는 한칸 왼쪽으로 이동한\
    것처럼 보이지만 실제로 커서 오른쪽의 문자는 그대로!
P $ $라는 문자를 왼쪽에 추가하기
"""
import sys

stack_1 = list(sys.stdin.readline().rstrip()) #첫번째 스택에 문자열 넣기
stack_2 = [] #빈 배열 -> 커서 기준으로 나눠 담을 것! 지금은 커서가 맨 뒤이므로 빈 배열

cursor_idx = len(stack_1)-1

for _ in range(int(sys.stdin.readline())):
    order = list(sys.stdin.readline().split())
    if order[0]=="L" :
        if stack_1: #커서 앞에 배열이 존재할 때에만
            stack_2.append(stack_1.pop()) #stack_1 맨 뒤에 있는 것을 빼서 stack_2 에 넣기
    elif order[0]=="D":
        if stack_2: #커서 뒤에 배열이 존재할 때만
            stack_1.append(stack_2.pop())
    elif order[0]=="B":
        if stack_1:
            stack_1.pop()
    else:
        order_str = order[1]
        stack_1.append(order_str)

#stack_1 과 뒤집은 stack_2를 합치기
# => 뒤집어서 합치는 이유는 insert 를 쓰지 않기 위해서 order이 L인 경우에 append를 사용했기 때문!
stack_1.extend(reversed(stack_2))
print(''.join(stack_1))
