def sec_to_utc(total_sec):
    def add_front_zero(num):
        str_num = str(num)
        return'0' +str_num if len(str_num) ==1 else str_num

    hour = total_sec // 3600
    minu = (total_sec % 3600) // 60
    sec = (total_sec % 3600) % 60
    return add_front_zero(hour) + ":" + add_front_zero(minu) + ":" +add_front_zero(sec)

def utc_to_sec(s):
    hour, minu, sec = map(int, s.split(":"))
    return hour * 3600 + minu * 60 + sec

def solution(play_time, adv_time, logs):
    time_stamp = [0] * 720000
    for log in logs:
        start, end =  log.split('-')
        
        time_stamp[utc_to_sec(start)] += 1
        time_stamp[utc_to_sec(end)] -= 1
    for i in range(1, len(time_stamp)):
        time_stamp[i] += time_stamp[i-1]
    for i in range(1, len(time_stamp)):
        time_stamp[i] += time_stamp[i - 1]
    max_value = 0
    start_time = 0
    total = 0
    adv = utc_to_sec(adv_time)-1
    for i in range(adv, len(time_stamp)):
        v = time_stamp[i]
        if i > adv:
            v  -= time_stamp[i - adv-1]
        if (max_value < v):
            max_value = v
            start_time = i-adv
        
    return sec_to_utc(start_time)

print(solution("00:00:30","00:00:02",["00:00:01-00:00:02", "00:00:00-00:00:02"] ))
print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"] ))
print(solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"] ))
print(solution("50:00:00","50:00:00",["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"] ))