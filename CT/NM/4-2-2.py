n = list(input())
num = 1
result = 0

for i in range(len(n)-1,-1,-1):
    result += int(n[i])*num
    num*=2

result *= 17

result_after = []
result_str = ""

while result>=2:
    num = result%2
    result = result//2
    result_after.insert(0,num)
result_after.insert(0,result)

for i in range(len(result_after)):
    result_str += str(result_after[i])

print(result_str)

