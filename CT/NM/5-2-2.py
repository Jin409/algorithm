#n은 학생의 수, m은 몇번 입력할지, k번 이상 벌칙을 받으면 벌금!
n,m,k = map(int,input().split())

stu_list = [0]*(n+1)
charge = []

for i in range(m):
    #벌점
    stu_num = int(input())
    stu_list[stu_num]+=1
    if k in stu_list:
        charge.append(stu_num)
if len(charge)==0:
    print(-1)
else:
    print(charge[0])