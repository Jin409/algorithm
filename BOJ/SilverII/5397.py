t = int(input())


for _ in range(t):
    password = input().strip()
    left, right = [], []

    for i in range(len(password)):
        if password[i] == "<":
            if left:
                right.append(left.pop())
        elif password[i] == ">":
            if right:
                left.append(right.pop())
        elif password[i] == "-":
            if left:
                left.pop()
        else:
            left.append(password[i])
    reversed(right)
    left.extend(right)
    print(''.join(left))
