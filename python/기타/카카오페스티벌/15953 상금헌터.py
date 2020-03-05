T = int(input())
money_1 = [0] [500] + [300]*2 +[200] * 3 + [50] * 4 + [30] * 5+[10]*6 + [0] * 100
money_2 = [0] + [512] + [256]*2 + [128]*4 + [64]*8 + [32]* 16 + [0] * 50

for tc in range(T):
    a, b = map(int, input().split())
    print((money_1[a] + money_2[b])*10000)