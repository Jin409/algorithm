'''
x번 카드 / y번 카드 골라서 쓰여진 수를 더하기
계산한 값을 두 카드에 덮어쓰기

카드에 쓰여 있는 수를 모두 더한 것이 점수 => 최대한 작게 만들어야
'''

n,m = map(int,input().split())
arr = list(map(int,input().split()))


# 매번 가장 작은 수를 더하면 될듯


for _ in range(m):
    arr.sort()
    num_1, num_2 = arr[0], arr[1]
    arr[0] = num_1+num_2
    arr[1] = num_1+num_2

print(sum(arr))

