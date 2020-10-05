'''
23분 컷
'''
def solution(new_id):
    new_id = new_id.lower()
    temp = ''
    for chr in new_id:
        if (97 <= ord(chr) <= 122) or 48 <= ord(chr) <= 57 or chr == "-" or chr == "." or chr == "_":
            temp += chr
    answer = ''
    prev = ""
    for chr in temp:
        if prev != "." and chr == ".":
            answer += chr
        elif chr != ".":
            answer += chr
        prev = chr
    if len(answer) and answer[0] == ".":
        answer = answer[1:]
    if len(answer) and answer[-1] == ".":
        answer = answer[:-1]

    if not len(answer):
        answer = "a"
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]

    return answer

print(solution("1"))

