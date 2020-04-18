def solution(lines):
    dic = {}
    cnt = 1
    for line in lines:
        temp =line.split()
        hms = temp[1].split(":")
        s = int(float(temp[2][:-1]) * 1000)
        adj_time = int((60*60 *float(hms[0]) + 60 * float(hms[1]) + float(hms[2]))*1000)  #초단위로 변환
        print(hms, s, adj_time-s+1, adj_time)
        print(cnt)
        cnt+=1
        for i in range((adj_time-s+1)//1000, adj_time//1000 + 1):
            print(i)
            if dic.get(i) is None:
                dic[i] = 1
            else:
                dic[i] += 1
    print(dic)
    answer = 0
    return answer

print(75660.748 - 2.31)
solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"])
