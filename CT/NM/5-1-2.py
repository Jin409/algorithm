n = int(input())
num_list = []

for i in range(n):
    num = int(input())
    num_list.append(num)

before = num_list[0]
cnt=1
max_list = []

for i in range(1,len(num_list)):
    if before*num_list[i]>0:
        cnt+=1
    else:
        max_list.append(cnt)
        cnt=1
    before = num_list[i]
max_list.append(cnt)

print(max(max_list))
