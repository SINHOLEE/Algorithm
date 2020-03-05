N = int(input())
my_time = input()

hours = float(my_time[:2])

mins = int(my_time[3:5])
if mins == 30:
    hours += 0.5
if my_time[9] == '+':
    hours -= float(my_time[10:])
else:
    hours += float(my_time[10:])


for _ in range(N):
    temp = input()
    if temp[3] == '+':
        new_hours = hours + float(temp[4:])
    else:
        new_hours = hours - float(temp[4:])
    if new_hours > float(24):
        new_hours -= float(24)
    elif new_hours < float(0):
        new_hours = float(24) + new_hours

    s = ''
    new_hours = str(new_hours)
    if new_hours == '24.0':
        s = '00:00'
    else:
        for i in range(len(new_hours)):
            if new_hours[i] == '.':
                if i == 1:
                    s += '0'
                    s += str(new_hours[i-1])
                    s += ':'
                else:
                    s += str(new_hours[:i])
                    s += ':'
                if new_hours[i+1] == '5':
                    s += '30'
                else:
                    s += '00'
            else:
                continue
    print(s)