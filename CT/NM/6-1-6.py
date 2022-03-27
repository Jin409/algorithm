origin_a = list(map(int,input()))
max_result = 0

def change(a):
    result = 0
    num = 1
    for i in range(len(a)-1,-1,-1):
        result += a[i]*num
        num*=2
    return result

def copy():
    global a
    a = []
    for i in range(len(origin_a)):
        a.append(origin_a[i])

for i in range(len(origin_a)):
    copy()
    if a[i]==0:
        a[i]=1
    else:
        a[i]=0

    max_result = max(change(a),max_result)

    
    
print(max_result)