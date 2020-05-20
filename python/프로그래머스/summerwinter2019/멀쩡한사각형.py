from decimal import *
#

def solution(w,h):
    big = max(w, h)
    small = min(w, h)
    cnt = 0
    original = small / big
    temp = original
    for i in range(1, big+1):
        new_temp = original * i
        if abs(int(new_temp)-new_temp) <0.00000001:
            temp = new_temp
            cnt+=1
            continue
        if int(new_temp) == int(temp):
            cnt += 1
        else:
            cnt += 2
        temp = new_temp

    return w * h - cnt


print(solution(100000000, 1))
