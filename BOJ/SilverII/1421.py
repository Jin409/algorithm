# 나무의 길이를 모두 같게 만들어야 한다. 
# 단 한번의 판매 기회 
# 나무를 한번 자를 때 c원이 들고, k(개의 나무)*w(단위당가격)*l(길이)

n,c,w = map(int,input().split()) #n개의 나무 c 자를 때 드는 가격 w 단위당 가격

trees = [
    int(input())
    for _ in range(n) #가지고 있는 나무의 길이
]

max_tree = max(trees)
max_benefit = 0

for i in range(1,max_tree+1):
    benefit = 0
    cnt_trees = 0
    cost = 0
    length = i #나무 길이의 단위
    for j in range(len(trees)):
        cnt,remain = trees[j]//length,trees[j]%length
        if not remain: #나머지가 없다면
            cost = (cnt-1)*c
        else:
            cost = cnt * c

        new_benefit = (length*cnt*w)-cost

        if new_benefit>0:
            benefit+=new_benefit
    max_benefit = max(max_benefit,benefit)

print(max_benefit)