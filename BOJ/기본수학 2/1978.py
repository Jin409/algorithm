n = int(input())
cnt=0
num_list = list(map(int,input().split()))
for i in range(n):
    num = num_list[i]
    is_it_decimal = True
    if num==1:
            is_it_decimal=False
    else:
        for j in range(2,num):
            if num%j==0:
                is_it_decimal=False
    if is_it_decimal==True:
        cnt+=1
print(cnt)

