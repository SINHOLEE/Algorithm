n = int(input())
questions = []
for _ in range(n):
    num, strike, ball = map(int, input().split())
    questions.append((num, strike, ball))
cnt = 0
visited = [0] * 10
for i in range(1,10):
    for j in range(1,10):
        if i == j:
            continue
        for k in range(1,10):
            if i == k or j == k:
                continue
            flag2 = True
            for question in questions:
                my_think = (i, j, k)
                my_strike = 0
                my_ball = 0
                num, strike, ball = question
                num = str(num)
                for idx1 in range(3):
                    for idx2 in range(3):
                        if idx1 == idx2:
                            if my_think[idx1] == int(num[idx2]):
                                my_strike += 1
                                break
                        else:
                            if my_think[idx1] == int(num[idx2]):
                                my_ball += 1
                                break
                if my_ball == ball and my_strike == strike:
                    continue
                else:
                    flag2 = False
                    break
            if flag2:
                cnt += 1

print(cnt)