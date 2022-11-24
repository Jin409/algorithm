n,k = map(int,input().split())

arr = list(input())

cnt = 0

for i in range(n):
    flag = False
    if arr[i] == "P":

        for j in range(k,0,-1):
            idx = i-j

            if idx < 0:
                continue

            if flag == False and arr[idx] == "H":
                arr[idx] = 0
                cnt+=1
                flag = True
                break

        if flag:
            continue

        for j in range(1,k+1):
            idx = i+j

            if idx > n-1:
                continue

            if flag == False and arr[idx] == "H":
                arr[idx] = 0
                cnt+=1
                flag = True
                break


print(cnt)