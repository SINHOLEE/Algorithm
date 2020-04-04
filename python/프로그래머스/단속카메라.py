def solution(routes):
    s_routes = sorted(routes, key=lambda x: x[1])
    temp = s_routes[0][1]
    answer = 1
    for i in range(1, len(routes)):
        if s_routes[i][0] > temp:
            temp = s_routes[i][1]
            answer += 1
    return answer


solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]])
