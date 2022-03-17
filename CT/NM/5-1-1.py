#연속하는 수 중 최장 길이 구하기

n = int(input())
num_list = []
for i in range(n):
    num = int(input())
    num_list.append(num)


cnt = 1
before = num_list[0]
max_list = []

for i in range(1,len(num_list)):
    if num_list[i]==before:
        cnt+=1
    else:
        max_list.append(cnt)
        cnt=1
    before = num_list[i]

max_list.append(cnt)

print(max(max_list))