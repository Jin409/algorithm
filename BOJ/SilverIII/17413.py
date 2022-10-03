word = list(input())#입력받을 문자열

idx = 0
start = 0

stack = []

while idx < len(word):
    if word[idx] == "<":
        idx+=1
        while word[idx] != ">":
            idx+=1
        idx+=1
    elif word[idx].isalnum():
        start = idx
        while idx < len(word) and word[idx].isalnum():
            idx+=1
        tmp = word[start:idx]
        tmp.reverse()
        word[start:idx] = tmp
    else:
        idx +=1

print(''.join(word))