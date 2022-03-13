# 재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

# 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

n = int(input()) #3의 k승

star = "***\n* *\n***"

def star(n):
    star = "***\n* *\n***"
    if n==3:
        print(star)
    else:
        star()

for i in range(1,n+1):
    for j in range(1,n+1):
        if i%3==0 and j%3==0:
            if :
                print(' ',end=' ')
            else:
                print("***\n* *\n***",end=' ')
        