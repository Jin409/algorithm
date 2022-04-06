# 한 단어가 다른 단어의 접두어가 되지 않는 집합.

n = int(input()) #단어의 수
words = []

for i in range(n):
    words.append(input()) #단어들을 배열에 추가

words = set(words) #중복을 제거하기 위해 집합으로 형 변환
words = list(words)
words.sort(key=len)

"""
틀린 풀이 : 처음에는 어떤 한 단어를 기준으로 잡고, 그 단어로 시작하지 않는 단어들을 \
    전부 어떤 배열에 넣은 뒤에, 그 배열에서도 서로 겹치게 시작하지 않도록 해야 한다고 생각.
    그러나 이렇게 할 경우에 생각대로 진행이 되지 않았음. (어떤 단어를 먼저 보냐에 따라 오류가 난듯)

참고한 풀이 : 길이별로 정렬한 뒤, 접두사가 아닌 단어들만 추가 (문제를 잘못 보고 이해했던것같음.....)
"""

length = 0

for i in range(len(words)):
    flag = False 
    #길이대로 정렬했으므로 자신보다 긴 단어들만 확인 
    for j in range(i+1,len(words)):
        if words[j].startswith(words[i]):
            flag=True
            break

    if not flag:
        length+=1

print(length)

# max_len = 0

# #기준이 되는 단어 정하기
# for i in range(len(words)):
#     arr = []
#     for j in range(len(words)):
#         if i==j:
#             arr.append(words[i])
#         elif not words[j].startswith(words[i]) and not words[i].startswith(words[j]):
#             arr.append(words[j])
#     print(words[i],arr)
#     for u in range(len(arr)):
#         for k in range(len(arr)):
#             if u==k:
#                 continue
#             elif arr[k].startswith(arr[u]):
#                 arr[k]=" "
#     print(arr)
#     length=0
#     for i in range(len(arr)):
#         if arr[i]!=" ":
#             length+=1

#     max_len = max(length,max_len)

# print(max_len)