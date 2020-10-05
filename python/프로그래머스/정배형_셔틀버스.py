def time_to_string(time):
    hour = time // 60
    min = time % 60
    if len(str(hour)) == 2:
        hour = str(hour)
    else:
        hour = "0" + str(hour)

    if len(str(min)) == 2:
        min = str(min)
    else:
        min = "0" + str(min)
    return hour + ":" + min


def solution(n, t, m, timetable):
    answer = ''
    total = n*m
    buses = [540]
    while len(buses) != n:
        buses.append(buses[-1] + t)
    users = []
    for time in timetable:
        hour, minute = time.split(':')
        minutes = int(hour) * 60 + int(minute)
        users.append(minutes)
    buses.sort()
    users.sort()
    # print(buses, m)
    # print(users)

    for i in range(len(buses)):
        bus_in = 0

        # 마지막 버스에 대해서 작업하면 됨.
        if i == len(buses) - 1:
            remain_users = []
            for user in users:
                if user > buses[-1]:
                    continue
                remain_users.append(user)

            if len(remain_users) < m:
                return time_to_string(buses[-1])

            else:
                return time_to_string(users[m-1]-1)

        # 마지막 버스가 아니면 사람 태워서 보내기.
        else:
            bus = buses[i]
            bus_in = []
            for _ in range(m):
                if _ > len(users)-1:
                    continue
                if users[_] < bus:
                    users.pop(0)

    return answer