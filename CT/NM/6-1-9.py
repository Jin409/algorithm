n = int(input())

nums = []
cnt_num = []

for i in range(n):
    num = int(input())
    nums.append(num)

############################################

#숫자를 일의 자리, 백의 자리. .. 로 쪼개기
def change(num):
    result = [0]*5
    divisor = 10
    divisor2 = 1
    for i in range(5):
        result[i] = num%divisor//divisor2
        divisor*=10
        divisor2*=10
    return result

#캐리가 발생하지 않는지 확인
def check(num1,num2,num3):
    num1_arr = change(num1)
    num2_arr = change(num2)
    num3_arr = change(num3)
    for i in range(5):
        if num1_arr[i]+num2_arr[i]+num3_arr[i]>=10:
            return False
    return True

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if check(nums[i],nums[j],nums[k]):
                cnt_num.append(nums[i]+nums[j]+nums[k])

if len(cnt_num)==0:
    print(-1)
else:
    print(max(cnt_num))