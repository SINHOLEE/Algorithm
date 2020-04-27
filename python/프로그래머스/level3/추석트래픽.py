def line_to_time(line):
    temp = line.split()
    hms = temp[1].split(":")
    s = int(float(temp[2][:-1]) * 1000)
    adj_time = int((60 * 60 * float(hms[0]) + 60 * float(hms[1]) + float(hms[2])) * 1000)  # 초단위로 변환
    # print(hms, s, adj_time-s+1, adj_time)
    return adj_time, s


def solution(lines):
    res = 0
    bucket = []
    for line in lines:
        bucket.append(line_to_time(line))

    for adj_time, s in bucket:
        for end_time_stamp in range(adj_time-s+1, adj_time+1, 1000):
            start_time_stamp = end_time_stamp - 999
            temp = 0
            for adj_time1, s1 in bucket:
                if start_time_stamp > adj_time1 or end_time_stamp < adj_time1-s1+1:
                    continue
                temp += 1
            if temp > res:
                res = temp
    return res


solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])
