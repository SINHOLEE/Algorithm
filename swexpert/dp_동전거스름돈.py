from time import time
start = time()



last = [1, 4, 6]

target = 10000000
memo = [9999999999999999999999] * (target + 1)


def solution(target):
    global memo,count
    for i in range(1, target+1):
        if i == 1 or i == 4 or i == 6:
            memo[i] = 1
        else:
            j = 0

            while True:
                count +=1
                if i - last[j] > 0:  # 현재 타겟에 1, 4, 6을 빼도 0보다 크다면,
                    memo[i] = min(memo[i-last[j]], memo[i])
                j += 1
                if j == 3:
                    break
            memo[i] +=  1
count = 0
solution(target)
print(memo[target])
print(count)
print(time()-start)