a,b,c = map(int,input().split())

#날짜가 앞선 경우
if a<11 or (a==11 and b<11) or (a==11 and b==11 and c<11):
    print(-1)

else:
    day = a-1-11 # 완전히 24시간이 소요되는 날짜를 구한다.

    minutes = 0
    minutes += day*60*24 # 완전히 24시간이 소요되는 날들의 분
    minutes += (60-11)+(24-11-1)*60 # 11일 minutes 더하기
    minutes += b*60+c

    print(minutes)