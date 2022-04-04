# 가장 왼쪽에서 정수만큼 떨어진 거리만 물이 샌다.
# 길이가 L인 테이프를 무한개 갖고 있음.
# 테이프 좌우 0.5 만큼 간격을 줘야 한다.
# 항승이가 필요한 테이프의 최소 개수 (겹쳐서 붙이기 가능)

"""

locas 라는 배열에 물이 새는 위치들을 넣어 오름차순으로 정렬 -> 왼쪽부터 샌다고 했으므로
cnt = 1인 이유는 start 부터 시작하기 때문.
간격을 0.5씩은 줘야 한다고 했으므로 0.5 * 2 = 1
따라서 테이프 길이인 l-1 보다 

"""

n,l = map(int,input().split()) #물이 새는 곳의 개수와 테이프의 길이
locas = list(map(int,input().split())) #물이 새는 위치들의 배열
locas = sorted(locas)

cnt = 1
start = locas[0] #시작점

for i in range(1,n):
    end = locas[i]
    if end - start <= l-1:
        continue
    else:
        cnt+=1
    start = end

print(cnt)

