from collections import deque
delta = [1,-1,2]
n,k = map( int, input().split())
subin = deque([n,-1])
location_bro = k
min_cnt = 9999
cnt = 0
flag = False
visited_odd = [0] * 500001
visited_even = [0] * 500001
visited_odd[n] = 1
while subin:

    if location_bro > 500000:
        break
    if min_cnt <= cnt:
        break
    if len(subin) == 1:
        break
    location_subin = subin.popleft()
    if location_subin == -1:
        cnt += 1
        location_bro += cnt
        subin.append(-1)
        continue
    temp = location_bro
    new_cnt = cnt
    while True:
        if temp > 500000:
            break
        if new_cnt > min_cnt:
            break
        if temp > location_subin:
            break
        if location_subin == temp:
            if min_cnt > new_cnt:
                min_cnt = new_cnt
            break
        for _ in range(2):
            new_cnt += 1
            temp += new_cnt

    if cnt % 2: # 홀수
        for k in range(3):
            if k == 2: # 두배
                new_subin = location_subin * 2
            else:
                new_subin = location_subin + delta[k]
            if 0 <= new_subin <= 500000 and visited_odd[new_subin] == 0:
                visited_odd[new_subin] = 1
                subin.append(new_subin)

    else:
        for k in range(3):
            if k == 2:  # 두배
                new_subin = location_subin * 2
            else:
                new_subin = location_subin + delta[k]
            if 0 <= new_subin <= 500000 and visited_even[new_subin] == 0:
                visited_even[new_subin] = 1
                subin.append(new_subin)
if min_cnt >= 9999:
    print(-1)
else:
    print(min_cnt)

