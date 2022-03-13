def find_decimal(i):
    if i==1:
        return False
    else:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                return False
        return True
m,n = map(int,input().split())
for i in range(m,n+1):
    if find_decimal(i):
        print(i)
        
# 시간초과 오답 -> 함수로 바꿔서 굳이 내부 for 루프를 모두 돌 필요 없이 \
    # 소수가 아님이 드러나면 false 를 반환하도록 함. + 2부터 i 까지 for 루프를 돌 필요 없이
    # 제곱근만을 탐색해도 소수인지 아닌지 알 수 있음. 
# m,n = map(int,input().split())
# for i in range(m,n+1):
#     is_it_decimal = True
#     if i==1:
#         is_it_decimal=False
#     else:
#         for j in range(2,int(i**0.5)+1):
#             if i%j==0:
#                 is_it_decimal=False
#     if is_it_decimal==True:
#         print(i)
