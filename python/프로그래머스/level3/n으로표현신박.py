def solution(N, number):
    S = [{0}]
    for i in range(1, 9):
        lst = {int(str(N)*i)}
        for X_i in range(1, i):
            for x in S[X_i]:
                for y in S[i - X_i-1]:
                    lst.add(x + y)
                    lst.add(x - y)
                    lst.add(x * y)
                    if y != 0: lst.add(x // y)
        if number in set(lst):
            return i
        S.append(lst)
    return -1

print(solution(5, 72))
