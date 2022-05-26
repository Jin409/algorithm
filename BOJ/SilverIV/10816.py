"""
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
m = int(input())
matching = list(map(int,input().split()))

arr.sort()

def find_num(start,end,num,cnt):
    if start > end:
        return cnt

    mid = (start+end)//2

    if arr[mid] > num:
        return find_num(start,mid-1,num,cnt)
    elif arr[mid] < num:
        return find_num(mid+1,end,num,cnt)
    else:
        find_num(start,mid-1,num,cnt)
        find_num(mid+1,end,num,cnt)

for num in matching:
    # print(find_num(1,n-1,num,0),end=' ')
    find_num(1,n-1,num,0)