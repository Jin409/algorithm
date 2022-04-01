n,m,d,s= map(int,input().split()) # n명의 사람 m개의 치즈
#어떤 치즈를 먹었는지 d번 기록 / 어떤 사람이 아팠는지 s번 기록.
# 완벽한 기록은 아님. 
# 약이 최대 몇개 필요할까.
# 1초가 지나야 아프기 시작한다. 

cheeze = []
for i in range(d):
    # 몇번째 사람이 / 몇번째 치즈를 / 언제 먹었는지
    # p,ch,t
    cheeze_tuple = tuple(map(int,input().split()))
    cheeze.append(cheeze_tuple)


#특정한 사람이 먹은 치즈
def find(person,time):
    ate_cheeze = []
    for i in range(d):
        p,ch,t = cheeze[i]
        if person == p and t<time:
            ate_cheeze.append(ch)
    return ate_cheeze

people = [0]*50
sick_people = []
for i in range(s):
    #몇번째 사람이 언제 아팠는지
    p,t = tuple(map(int,input().split()))
    sick_people.append(p)
    # sick.append(sick_tuple)
    ate_cheeze = find(p,t) #아픈 사람이 먹은 치즈 전부 + 아픈 후에 먹은 치즈 빼고
    ate_cheeze = set(ate_cheeze)
    people[p] =  list(ate_cheeze)#아픈 사람이 먹은 치즈 목록 기록 + 중복 제거


# 아픈 사람들이 공통적으로 먹은 치즈를 찾고 -> 그 중에서도 아픈 시점 전에 먹은 치즈 -> 해당 치즈를 먹은 
# 모든 사람들이 아플 것이라고 가정하여 약의 개수


#공통적으로 먹은 치즈 찾기
idx = sick_people[0]
sick_people_cheeze = people[idx]

find_common_cheeze = [
    sick_people_cheeze[j]
    for j in range(len(sick_people_cheeze))
]

for i in range(1,s):
    new_arr = []
    idx = sick_people[i]
    #아픈 사람이 먹은 치즈 
    sick_people_cheeze = people[idx]
    for j in range(len(sick_people_cheeze)):
        if sick_people_cheeze[j] in find_common_cheeze:
            new_arr.append(sick_people_cheeze[j])
    find_common_cheeze = []
    for j in range(len(new_arr)):
        find_common_cheeze.append(new_arr[j])

#아픈 사람이 먹은 치즈를 먹은 사람 전부 카운트하기 
max_cnt = 0 # 우선 확실히 아픈 사람을 더한다.
# 원인이 되는 치즈를 먹은 사람을 모두 더하기
for i in range(len(find_common_cheeze)):
    cnt=s
    cnt_people = [
        sick_people[j]
        for j in range(len(sick_people))
    ]
    rot_cheeze = find_common_cheeze[i]
    for j in range(len(cheeze)):
        p,ch,t = cheeze[j] 
        #아프지 않은 사람
        if p not in cnt_people and ch==rot_cheeze:
            cnt+=1
            cnt_people.append(p)
    max_cnt = max(max_cnt,cnt)
            
print(max_cnt)

    
# 같은 치즈를 또 먹는 경우를 고려하지 않았음 => cnt_people 생성해서 이미 센 사람을 제외시키도록 함. 