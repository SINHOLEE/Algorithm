def solution(p):
    p+=1
    while True:
        if len(set(list(str(p)))) == len(list(str(p))):
            break
        p+=1
    return p


print(solution(2015))
