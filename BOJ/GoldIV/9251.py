'''
부분 수열 찾기 => 부분 수열 중 가장 긴 것
'''

word1 = input()
word2 = input()

min_len = min(len(word1),len(word2))

dp = [[0]]*(min_len+1) #길이가 인덱스

for i in range(min_len):
    if word1[i] in word2 and word1[i] not in dp[1]:
        dp[1].append(word1[i])
dp[1] = dp[1][1:]

for i in range(1,min_len+1):
    # word1 에서 다음 글자를 더할지 말지 결정
    # 더 이상 찾을 수 있는 부분수열이 존재하지 않으면 break
    # 같은 알파벳이 여러개 있으면 어떻게 해야 하지..?
    # for j in range(len(dp[i-1])):
        # if word1.count(dp[i-1][j]) >=2 or word2.count(dp[i-1][j]) >=2:

    for j in range(min_len):
        # 부분수열에 포함되지 않는 문자열
        if word1[j] not in dp[i-1]:
            continue
        # 부분수열에 포함되는 문자열
        # 지금 보고 있는 인덱스 i 이후로 dp[i-1]에 포함되는 글자가 있는지 찾기
        word1[i]

# print(dp)
# 답은 0이 아닌 인덱스 중 가장 큰 것 출력하려고

