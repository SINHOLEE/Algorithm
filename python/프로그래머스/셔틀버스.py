def decode(num):
    hour = num // 60
    minute = num % 60
    if hour < 10:
        hour = '0' + str(hour)
    else:
        hour = str(hour)
    if minute < 10:
        minute = '0' + str(minute)
    else:
        minute = str(minute)

    return hour + ":" + minute


def string_to_timelist(string):
    string = list(map(int, string.split(':')))
    return string[0] * 60 + string[1]


def solution(n, t, m, timetable):
    answer = ''
    new_list = []
    for time in timetable:
        new_list.append(string_to_timelist(time))
    new_list.sort()
    start_time = 9 * 60
    for i in range(n): # n번의 버스가 올겁니다.
        if i != 0:
            start_time +=  t
        temp = []
        for j in range(m): # m명까지 태울 수 있습니다.
            if len(new_list) == 0:
                continue
            if new_list[0] <= start_time:
                temp.append(new_list.pop(0))
    if len(temp) == 0:
        res = start_time
    else: #
        if len(temp) < m:
            res = start_time
        else:
            for j in range(m-1, 0, -1):
                if temp[j] == temp[j-1]:
                    continue
                else:
                    res = temp[j-1]
                    break
            else:
                res = temp[0] - 1

    return decode(res)


print(solution(		2, 1, 1, ["24:00", "24:00", "24:00"]))