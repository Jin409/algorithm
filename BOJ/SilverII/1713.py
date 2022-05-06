"""
특정 학생 추천 => 추천받은 학생의 사진이 게시됨
비어있는 틀이 없으면 추천 횟수가 가장 적은 학생이 삭제
추천 받은 횟수가 같은 경우에는 먼저 게시된 학생 삭제
삭제되면 횟수 0으로 바뀜
최종 후보가 누구인지 결정
"""

n = int(input()) #사진틀의 개수
k = int(input()) #총 추천 횟수
recommends = list(map(int,input().split()))

for reco in recommends:
    if 