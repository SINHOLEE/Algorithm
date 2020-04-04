def solution(people, limit):
    people.sort()
    s = 0
    e = len(people) - 1
    answer = 0
    while s <= e:
        if e == s:
            answer += 1
            break
        if people[e] + people[s] <= limit:
            s += 1
        e -= 1
        answer += 1
    return answer


print(solution([40, 40, 80], 160))
