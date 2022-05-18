n = int(input())
arr = list(map(int,input().split()))
result_arr = []

def find_arr(result,cnt):
    if cnt==n:
        if not result:
            pass
        else:
            result_arr.append(sum(result))
    else:
        if not result:
            find_arr([arr[cnt]],cnt+1)
            find_arr(result,cnt+1)
        else:
            if result[-1] <= arr[cnt]:
                find_arr(result.append(arr[cnt]),cnt+1)
                find_arr(result,cnt+1)
            else:
                find_arr(result,cnt+1)

find_arr([],0)
print(max(result_arr))
