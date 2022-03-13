def find_decimal(i):
    if i==1:
        return False
    else:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                return False
        return True
    
while True:
    n = int(input())
    if n==0:
        break
    cnt=0
    for i in range(n,(n*2)+1):
        if find_decimal(i):
            cnt+=1
    print(cnt)
