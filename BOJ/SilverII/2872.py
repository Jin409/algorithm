import sys

input = sys.stdin.readline

n = int(input())
books = [
    int(input())
    for _ in range(n)
]

ans = 0
min_book = 1 #어디까지 정렬했는지 확인

for i in range(n):
    if books[i] - min_book == 0 or books[i] - min_book == 1:
        min_book = books[i]
        continue
    elif books[i] - min_book < 0:
        continue
    else:
        ans += (books[i] - min_book)
        min_book = books[i]

print(ans)