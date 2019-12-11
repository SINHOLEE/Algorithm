message = 'the output a message may not exceed the K=character limit'
K = 11

def solution(message, K):
    # write your code in Python 3.6
    res = ''
    temp = ''
    cnt = 0
    for i in range(len(message)):
        cnt += 1
        temp += message[i]
        if cnt <= K:
            if i == len(message) - 1 or message[i+1] == ' ' :
                res += temp
                temp = ''
        else:
            break

    return res
print(solution(message,K))