n =2
t =10
m =2
timetable = ['09:10', '09:09', '08:00']


def solution(n, t, m, timetable):
    new_tt = []
    for time in timetable:
        a = int(time[:2]) * 60
        a += int(time[3:])
        new_tt.append(a)
    new_tt.sort()
    # 09:00 == 540
    my_time = 540
    round = 0
    for i in range(n):
        mm = m
        while True:
            if mm == 0:
                break
            if mm == 1 and i == n-1:
                cnt = 0
                for k in new_tt:
                    if  my_time + (i * t) >= k:
                        answer = k - 1
                        break
                else:
                    answer = my_time + (i*t)
                    break

            if len(new_tt) != 0 and new_tt[0] <= my_time + (t * i):
                new_tt.pop(0)
            mm -= 1

    front = answer // 60
    if front <= 9:
        front = "0"+str(front)
    else:
        front = str(front)

    back = answer % 60
    if back <= 9:
        back = '0' + str(back)
    else:
        back = str(back)

    temp = front + ':' + back

    return temp

print(solution(n,t,m,timetable))