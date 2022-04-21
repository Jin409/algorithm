"""
n명 (번호가 있다)
i번 인사하면 L[i]만큼 체력을 잃고
J[i] 만큼 기쁨을 얻음. 
체력은 100 그 안에서 해야 함.
최대 기쁨을 출력.
"""

n = int(input())
L = list(map(int,input().split())) #체력을 잃음
J = list(map(int,input().split())) #기쁨을 얻음
health = 100
joy = 0
idx = 0
new_arr = []

for i in range(n):
    new_arr.append((i,J[i]-L[i])) #인덱스와 차를 저장

new_arr.sort(key=lambda x:x[1], reverse=True) #오름차순 정렬 

while True:
    p_idx,lj_diff = new_arr[idx]
    health-=L[p_idx]
    if health<=0 or idx>=len(new_arr):
        break
    joy += J[p_idx]
    idx+=1

print(joy)