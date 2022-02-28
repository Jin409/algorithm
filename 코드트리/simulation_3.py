n,m= map(int,input().split())
num_list = list(map(int,input().split()))
array = []


max_calc = 0
def pick_nums(cnt,last_idx):
    global max_calc

    if cnt==m:
        max_calc = max(calc(),max_calc)
        return
    
    if last_idx==n:
        return

    for i in range(last_idx+1,n):

        num = num_list[i]
        #해당 숫자가 들어가거나
        array.append(num)
        pick_nums(cnt+1,i)

        #들어가지 않거나 
        array.pop()
    

#array에 값들이 존재하기 때문
def calc():
    result = array[0]
    for i in range(0,m-1):
        result = result^array[i+1]
    return result


pick_nums(0,-1)
print(max_calc)