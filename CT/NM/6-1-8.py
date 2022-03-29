n = int(input())

room_ppl = []
distance_arr = []

for i in range(n):
    ppl = int(input())
    room_ppl.append(ppl)

#start_idx는 시작하는 위치
def move(start_idx):
    distance = 0
    for i in range(len(room_ppl)):
        if start_idx > i:
            distance += (n-abs(start_idx-i))*room_ppl[i]
        elif start_idx == i:
            continue
        else:
            #시작하는 점보다 큰 경우 
            distance += abs(i - start_idx)*room_ppl[i]
    distance_arr.append(distance)

#각 방에서 시작해보기
for i in range(1,len(room_ppl)):
    move(i)

print(min(distance_arr))