


n = int(input())

def fact(num,result):
    if num==0:
        result = result*1
        print(result)
    else:
        result = result*num
        fact(num-1,result)

fact(n,1)