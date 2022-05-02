"""
최소 힙으로
가장 작은 값 출력, 그 값을 배열에서 제거하기
n 은 연산의 개수
x가 0이면 배열에서 가장 작은 값 출력, 제거
자연수라면 배열에 추가하는 연산
배열이 비어 있는데 x가 0이면 0 출력
"""
import sys
import heapq

n = int(input())
result = []
order_list = [
    int(sys.stdin.readline())
    for i in range(n)
]

for order in order_list:
    if order==0:
        if not result:
            print(0)
        else:
            print(heapq.heappop(result))
    else:
        heapq.heappush(result,order)



