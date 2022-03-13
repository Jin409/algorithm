n,b = map(int,input().split())
result = []
result_str = ""

while n>=b:
    num = n%b
    n = n//b
    result.insert(0,num)
result.insert(0,n)

for i in range(len(result)):
    result_str+=str(result[i])

print(result_str)