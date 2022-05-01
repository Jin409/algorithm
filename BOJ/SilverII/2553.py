n = int(input())

# 팩토리얼을 시간을 절약하여 구하는 법
cnt = 1 #무엇을 곱할지
result = 1 #팩토리얼의 결과

while cnt!=n:
    cnt+=1
    result*=cnt

result = str(result)

for i in range(len(result)-1,-1,-1):
    if result[i]!='0': #0이 아니라면
        print(result[i])
        break
    else:
        continue
