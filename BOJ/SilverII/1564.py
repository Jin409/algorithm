n = int(input())

"""
아래처럼 풀었는데 시간초과 남..!

다시 풀어보기 .......
다른 코드 참고함!
"""

result =1
for i in range(2,n+1):
    result*=i
    temp_result = str(result)
    while temp_result[-1]=="0":
        result //=10
        temp_result = str(result)
        
    result%=100000000000000000

print(str(result)[-5:])

    
# result = 1
# for i in range(1,n+1):
#     result *= i

# result = str(result)
# new_result = ""

# for i in range(len(result)-1,-1,-1):
#     if len(new_result)==5:
#         break
#     if result[i]!="0":
#         new_result += result[i]

# print(new_result[::-1])

