rotate = {1:-1, -1:1}

gear = [[]]
for i in range(4):
    temp = list(map(str, input()))
    gear.append(temp)
n = int(input())

for _ in range(n):
    gear_num, direction = map(int, input().split())
    linked_status = [0, 0, 0] # 0 은 아무상태도 아님, 1이면 서로 다름
    for k in range(1, 4):
        if gear[k][2] != gear[k+1][6]:  # 마주보고 있는 기어의 극성 확인
            linked_status[k-1] = 1
    i = gear_num
    j = gear_num
    if direction == 1:
        gear_dummy = gear[gear_num][:-1]
        a = gear[gear_num].pop(-1)
        gear[gear_num] = [a] + gear_dummy
        direction1 = -1
        direction2 = -1
    else:
        gear_dummy = gear[gear_num][1:]
        a = gear[gear_num].pop(0)
        gear[gear_num] = gear_dummy + [a]
        direction1 = 1
        direction2 = 1


    while True:
        if i == 4:
            break
        if linked_status[i-1] == 1:
            if direction1 == 1:
                gear_dummy = gear[i+1][:-1]
                a = gear[i+1].pop(-1)
                gear[i+1] = [a] + gear_dummy
                direction1 = -1
            else:
                gear_dummy = gear[i+1][1:]
                a = gear[i+1].pop(0)
                gear[i+1] = gear_dummy + [a]
                direction1 = 1

            i+=1
        else:
            break

    while True:
        if j == 1:
            break
        if linked_status[j-2] == 1:
            if direction2 == 1:
                gear_dummy = gear[j-1][:-1]
                a = gear[j-1].pop(-1)
                gear[j-1] = [a] + gear_dummy
                direction2 = -1
            else:
                gear_dummy = gear[j-1][1:]
                a = gear[j-1].pop(0)
                gear[j-1] = gear_dummy + [a]
                direction2 = 1

            j -= 1
        else:
            break


print(int(gear[1][0]) + int(gear[2][0]) * 2 + int(gear[3][0]) * 4 + int(gear[4][0]) * 8)
