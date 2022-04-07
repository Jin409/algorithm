n = int(input())

"""
아래처럼 풀었는데 시간초과 남..!

다시 풀어보기 .......
"""
result = 1
for i in range(2,n+1):
    result*=i
    
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

