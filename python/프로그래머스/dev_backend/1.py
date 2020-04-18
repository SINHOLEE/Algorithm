def solution(p,s):
    answer = 0
    for idx in range(len(p)):
        pp, ss = int(p[idx]),int(s[idx])
        if pp == ss:
            continue
        max_num = max(pp, ss)
        min_num = min(pp, ss)
        answer += min(max_num-min_num, min_num+10 -max_num)

    return answer

print(solution('82195', '64723'))