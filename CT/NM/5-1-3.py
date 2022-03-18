n = int(input())
num_list = []

for i in range(n):
    num = int(input())
    num_list.append(num)

before = num_list[0]
len_list = []
cnt=1

for i in range(1,n):
    if num_list[i]>before:
        cnt+=1
    else:
        len_list.append(cnt)
        cnt=1
    before = num_list[i]

len_list.append(cnt)

print(max(len_list))