"""
절단기의 높이 H
H보다 높은 나무는 (나무높이-H)만큼 잘림. H만큼 만큼 남음
"""
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
trees = list(map(int,input().split()))

start,end = 1,max(trees)

def cut_tree(start,end):
    if start > end:
        return end

    mid = (start+end)//2 #중간
    cnt = 0

    for tree in trees:
        if tree > mid:
            cnt += (tree-mid)

    if cnt >= m:
        return cut_tree(mid+1,end)
    else:
        return cut_tree(start,mid-1)

print(cut_tree(start,end))