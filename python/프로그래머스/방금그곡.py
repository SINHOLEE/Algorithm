from datetime import datetime


def string_to_minute(start, end):
    temp1 = datetime.strptime(start, '%H:%M')
    temp2 = datetime.strptime(end, '%H:%M')

    temp3 = temp2 - temp1
    return temp3.seconds // 60


def string_to_list(string):
    # 검증완료
    lis = []
    for s in string:
        if s == "#":
            lis[-1] += s
        else:
            lis.append(s)
    return lis


def solution(m, musicinfos):
    # 노래제목, minutes
    answer = []
    my_melody = string_to_list(m)
    for musicinfo in musicinfos:
        start, end, title, music = musicinfo.split(',')
        minutes = string_to_minute(start, end)
        radio_melody = string_to_list(music)
        if len(my_melody) > minutes:
            continue
        for i in range(minutes-len(my_melody)+1):
            for j in range(len(my_melody)):
                if my_melody[j] != radio_melody[(i+j) % len(radio_melody)]:
                    break
            else:
                if len(answer) == 0:
                    answer.append((title, minutes))
                else:
                    if answer[0][1] < minutes:
                        answer[0] = (title, minutes)
                break
    if len(answer) == 0:
        return "(None)"
    print(answer)
    return answer[0][0]



solution("CC#BCC#BCC#BCC#B", ["23:30,00:00,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])


print(string_to_minute("10:12", "11:01"))