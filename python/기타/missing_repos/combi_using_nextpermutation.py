# 1,2,3 일때 123 132 213 231 312 321순의 순열을 뽑는 알고리즘

nums = [1,2,3,4,5]
#1, 오름차순으로 정렬한다.
def combi(n,r):
    isEnd = True
    p = [0] * (n-r) + [1] * r

    # 3. 맨 뒤에 숫자부터 앞으로 탐색을 하면서 자리교환이 가능한 숫자를 찾는다.
    # 언제까지? 내림차순으로 정렬될때까지.
    p.sort()
    length = len(p)
    while True:
        # 1. i 찾기
        for num in range(length):
            if p[num]:
                print(nums[num], end=' ')
        print()

        for i in range(length-1, -1, -1):
            if i == 0:
                isEnd = False
                break
            if p[i-1] < p[i]:
                idx = i-1
                break
        if isEnd == False:
            break

        for k in range(length-1, -1,-1):
            if p[idx] < p[k]:
                p[idx], p[k] = p[k], p[idx]
                break
        my_end_idx = length-1
        idx+=1
        while idx < my_end_idx:
            p[idx], p[my_end_idx] = p[my_end_idx], p[idx]
            idx += 1
            my_end_idx -= 1

combi(5,3)