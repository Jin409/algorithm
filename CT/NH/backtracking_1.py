n,m,k = map(int,input().split())
distance = list(map(int,input().split()))

#말의 위치를 표시하기 위함.
list_mall = [1]*k
#가장 큰 점수
#점수는 어차피 무조건 최소 0이상이므로 0으로 할당. 

max_ans=0
#윷놀이 시작
#cnt는 움직인 만큼의 값!
def play(cnt):
    global max_ans

    max_ans = max(max_ans,calc_score())

    #다 움직였다면 종료
    if cnt==n:
        return

    #k 즉 말의 개수만큼 움직이고 말고를 결정할 수 있음. 
    for i in range(k):
        #이미 도달한 말은 움직일 필요가 없음. 
        if list_mall[i]>=m:
            continue
        #움직이는 횟수만큼 distance 리스트의 길이가 있으므로
        list_mall[i]+=distance[cnt]
        play(cnt+1)
        
        #list_mall[i]가 움직이지 않는 경우를 생각. 
        list_mall[i]-=distance[cnt]

#점수 세기
def calc_score():
    score = 0
    for mall in list_mall:
        if mall>=m:
            score+=1
    return score

play(0)
print(max_ans)





