# 종이에 모두 같은 수가 있는지 확인 -> 그대로 사용!
# 같은수가 아니라면 같은 크기 9개로 종이를 자름. -> 위의 조건 확인
# -1, 0, 1 로만 채워진 종이의 개수 출력

import sys
sys.setrecursionlimit(1000000)


n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

"""
전체가 같은지 확인해보고 같다면 이에 해당하는 숫자 증가시키기
같지 않다면 자르고 같은지 확인해보는 과정의 반복
자르는 범위를 어떻게 해야 할지 모르겠음..!
n 이 3의 제곱수인 것이 힌트일 것 같음.. 
1*1, 3*3, 9*9, 27*27.. -> 3씩 자르기

"""

result = [0,0,0] #-1, 0, 1의 개수 저장 (숫자+1 이 인덱스)

def check(x,y,n):
    temp = arr[x][y] #비교할 지점을 지정해줌
    for i in range(n):
        for j in range(n):
            #시작점 + ~
            if temp!=arr[x+i][y+j]:
                return False
    return True

# 범위를 나누기!
def devide(x,y,n):
    # 만약 전체가 똑같다면 (더 이상 분할할 필요 없는 경우)
    if check(x,y,n):
        idx = arr[x][y]
        result[idx+1] += 1
    else:
        # 또 분할해야 함!
        # 어떻게 9개로 나눌 수 있을까? 3*3이니까 3개씩으로 나누자
        for i in range(3):
            for j in range(3):
                devide(x+i*n//3,y+j*n//3,n//3)


devide(0,0,n) #가장 처음부터!
print(result[0])
print(result[1])
print(result[2])