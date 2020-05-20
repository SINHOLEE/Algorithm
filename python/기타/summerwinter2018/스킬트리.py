def solution(skill, skill_trees):
    answer = len(skill_trees)
    q1 = []
    cnt = 1
    for s in skill:
        q1.append(s)
        cnt+=1
    for tree in skill_trees:
        q = q1[:]
        for t in tree:
            if len(q):
                if t not in q:
                    continue
                else:
                    if t == q[0]:
                        q.pop(0)
                        continue
                    else:
                        answer -=1
                        break
    return answer


solution("CBD", ["BACDE", "CBADF", "AECB", "BDA", "CBAS"])
