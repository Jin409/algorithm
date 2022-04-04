# 가장 왼쪽에서 정수만큼 떨어진 거리만 물이 샌다.
# 길이가 L인 테이프를 무한개 갖고 있음.
# 테이프 좌우 0.5 만큼 간격을 줘야 한다.
# 항승이가 필요한 테이프의 최소 개수 (겹쳐서 붙이기 가능)

n,l = map(int,input().split()) #물이 새는 곳의 개수와 테이프의 길이
locas = list(map(int,input().split())) #물이 새는 위치들의 배열
locas = locas.sort()

for i in range(n):
    diff = locas[i+1] - locas[i] #두 위치의 길이 차이를 계산.
    if diff < l:
        
