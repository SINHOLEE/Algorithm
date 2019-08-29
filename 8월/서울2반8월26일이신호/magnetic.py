import sys
from pprint import pprint
sys.stdin = open("input.txt", "r")
sys.stdout = open('output.txt', 'w', encoding='utf-8')

for tc in range(1, 11):
    N = int(input())
    mat = []
    for n in range(N):
        temp = list(map(int, input().split()))
        mat += [temp]

    count = 0
    for i in range(len(mat)):
        mystack = []
        for j in range(len(mat[i])):
            if len(mystack) == 0:
                if mat[j][i] == 1:
                    mystack.append(1)
                elif mat[j][i] == 2:
                    pass
                else:
                    pass

            else:
                if mat[j][i] == 1:
                    pass
                elif mat[j][i] == 2:
                    mystack.pop()
                    count += 1
                else:
                    pass
    print('#{} {}'.format(tc, count))


