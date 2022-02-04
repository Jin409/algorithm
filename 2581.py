m = int(input())
n = int(input())
num_list = []
for i in range(m,n+1):
    is_it_decimal=True
    if i==1:
        is_it_decimal=False
    else:
        for j in range(2,i):
            if i%j==0:
                is_it_decimal=False
    if is_it_decimal==True:
        num_list.append(i)
if len(num_list)==0:
    print(-1)
else:
    print(sum(num_list))
    print(min(num_list))