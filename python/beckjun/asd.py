from collections import deque

q = deque()
q.p
age = int(input())
answer = [0] * 6
max_heat_beat = 220 - age
while True:
    heart_beat_string = ()
    print(heart_beat_string)
    if heart_beat_string[-1] != " ":
        break
    hb = int(heart_beat_string)
    hb_percentage = (hb / max_heat_beat) * 100
    print(hb)
    if 60 > hb_percentage:
        answer[5] += 1
    elif 68 > hb_percentage:
        answer[4] += 1
    elif 75 > hb_percentage:
        answer[3] += 1
    elif 80 > hb_percentage:
        answer[2] += 1
    elif 90 > hb_percentage:
        answer[1] += 1
    else:
        answer[0] += 1
print(answer)