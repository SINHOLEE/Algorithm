k = 10
room_number = [1,3,4,1,3,1]

def solution(k, room_number):
    visited = set()
    answer = []
    for room in room_number:
        if room not in visited:
            visited.add(room)
            answer.append(room)
        else:
            for i in range(room+1, k+1):
                if i not in visited:
                    visited.add(i)
                    answer.append(i)
                    break
    return answer


print(solution(k, room_number))