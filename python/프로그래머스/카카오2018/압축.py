def solution(msg):
    answer = []
    dic = {chr(ord("A")-1 + i): i for i in range(1, 27)}
    idx = 27
    while True:
        if msg == "":
            break
        start = 0
        for end in range(len(msg), -1, -1):
            if dic.get(msg[start:end]) is not None:
                answer.append(dic[msg[start:end]])
                if msg[:end] != "":
                    dic[msg[start:end+1]] = idx
                    idx += 1
                    msg = msg[end:]
                break

    return answer

msg = "TOBEORNOTTOBEORTOBEORNOT"
print(solution(msg))
