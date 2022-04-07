# 자기보다 큰 사람이 왼쪽에 몇명 있는지
# n명의 사람들

"""
키가 가장 큰 사람의 왼쪽에 몇명이 있는지부터 확인한다.
arr[i]==0 즉, 자신보다 큰 사람이 왼쪽에 없었다고 할 때는 키가 가장 큰\
    순서대로 보고 있으므로 가장 앞에 가는 것이 맞다.
arr[i]가 0이 아니라면 자신보다 큰 사람이 왼쪽에 몇명 있는지 확인하고,\
    그 위치에 가도록 한다. 그러나, 인덱스는 0부터 시작이므로 실제로는 members[i]+1 번째이지만,\
        members[i]번째에 i가 들어가도록 한다.
"""

n = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0)#자기보다 더 키 큰 사람이 왼쪽에 몇명? #arr의 인덱스가 키

#줄 선 순서대로 키를 출력

#맨 처음은 0이라서
#가장 키가 큰 사람 다음부터
members = [n]
for i in range(n-1,0,-1):
    if arr[i] ==0:
        members.insert(0,i)
    else:
        members.insert(arr[i],i)

for i in range(len(members)):
    print(members[i],end=' ')