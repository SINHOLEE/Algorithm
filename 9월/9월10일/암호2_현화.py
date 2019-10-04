import sys
sys.stdin = open('sample_input.txt', 'r')
sys.stdout = open('h_output.txt', 'w')


def chk_code():

    global r, idx
    password = []
    mag = 0
    for i in range(8):
        ratio = [0, 0, 0, 0]
        while code[idx] != '0':
            ratio[3] += 1
            idx -= 1
        while code[idx] == '0':
            ratio[2] += 1
            idx -= 1
        while code[idx] != '0':
            ratio[1] += 1
            idx -= 1
        if not mag:
            mag = min(ratio[1], ratio[2], ratio[3])
        ratio[0] += (7 * mag) - sum(ratio)
        idx -= ratio[0]
        if mag > 1:
            ratio = map(lambda x: x // mag, ratio)
        password.insert(0, decode[tuple(ratio)])
    return password


hextobin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
            '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

decode = {(3, 2, 1, 1): 0, (2, 2, 2, 1): 1, (2, 1, 2, 2): 2, (1, 4, 1, 1): 3, (1, 1, 3, 2): 4, (1, 2, 3, 1): 5,
          (1, 1, 1, 4): 6, (1, 3, 1, 2): 7, (1, 2, 1, 3): 8, (3, 1, 1, 2): 9}

result_list = []
for case in range(int(input())):
    N, M = map(int, input().split())
    codes = [list(input()) for _ in range(N)]
    bin_code = []
    visited = []
    result = 0
    for r in range(N):
        c = M - 1  # 마지막 인덱스
        flag = False
        temp = ''
        while c >= 0:  # 만약 마지막 인덱스가 0보다 작으면 멈추자
            if codes[r][c] != '0' and (codes[r - 1][c] == '0' or r == 0):  # 0이 아니고, 밑에 애도 0이 아니거나, 밑에가 없을 때
                flag = True
            if flag:
                temp = hextobin[codes[r][c]] + temp
            c -= 1
        if flag:
            bin_code.append(temp)

    for code in bin_code:
        idx = len(code) - 1
        while idx >= 0:
            if code[idx] != '0':
                password = chk_code()
                if password in visited:
                    continue
                chk = 0
                for i in range(8):
                    if not i % 2:
                        chk += password[i] * 3
                    else:
                        chk += password[i]
                if not chk % 10:
                    result += sum(password)
                    visited.append(password)
            else:
                idx -= 1
    result_list.append(result)

for i in range(len(result_list)):
    print(f'#{i+1} {result_list[i]}')

