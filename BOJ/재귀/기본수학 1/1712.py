def funcA():
    A,B,C = map(int, input().split())
    if B>=C:
        return -1
    else:
        return (A//(C-B)+1)
print(funcA())
