"""
학생에 대한 배열을 만들고 전부 sys.maxsize 로 선언 (min 비교를 수월하게 하기 위해서 0 사용 안함)
sys.maxsize 인 경우는 한번도 추천이 안된, 즉 추천 횟수 0으로 간주
추천을 for 문으로 돌면서 0번 추천된 경우에는 추천 횟수를 1로 업데이트.
그러나 이 과정에서 사진틀이 모자라다면, 추천 횟수가 가장 적은 인덱스들을 배열에 담고 오래된 순으로 확인
"""
import sys

n = int(input()) #사진틀의 개수
k = int(input()) #총 추천 횟수
recommends = list(map(int,input().split()))
student_num = [sys.maxsize]*101 #학생번호
cnt=0

for i in range(k):
    student = recommends[i] #추가되어야 하는 학생
    if student_num[student] == sys.maxsize: #카운트 횟수가 0
        if cnt==n:#사진틀 자리가 없다면
            min_value = min(student_num) #최소값
            min_arr = [j for j in range(101) if min_value==student_num[j]] #최소값에 해당하는 학생들 전부
            for u in range(i): #지금 확인하고 있는 추천 이전까지
                if recommends[u] in min_arr:
                    del_student = recommends[u]
                    student_num[del_student] = sys.maxsize
                    cnt-=1 #사진틀 공간 하나 생겼으니까
                    break #삭제하고 바로 브레이크
            for u in range(i):
                if recommends[u]==del_student:
                    recommends[u]=0
        student_num[student]=1
        cnt+=1
    else:
        student_num[student]+=1

for i in range(101):
    if student_num[i]!=sys.maxsize:
        print(i,end=' ')
