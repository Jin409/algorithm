a,b,c = map(int,input().split())

def solution(a,b):
    if b==1:
        return a%c
    else:
        result = solution(a,b//2)
        if b%2==0:
            return (result * result) %c
        else:
            return (result * result * a)%c

print(solution(a,b))