def isrightarr(current_arr, k):
    patturn = [
        '000' * k + '11' * k + '0' * k +'1' * k,  #0
        '00' * k + '11' * k + '00' * k + '1' * k,  #1
        '00' * k + '1' * k + '00' * k + '11' * k,  #2
        '0' * k + '1111' * k + '0' * k + '1' * k,  #3
        '0' * k + '1' * k + '000' * k + '11' * k,  #4
        '0' * k + '11' * k + '000' * k + '1' * k,  #5
        '0' * k + '1' * k + '0' * k + '1111' * k,  #6
        '0' * k + '111' * k + '0' * k + '11' * k,  #7
        '0' * k + '11' * k + '0' * k + '111' * k,  #8
        '000' * k + '1' * k + '0' * k + '11' * k,  #9
    ]

    for my_index in range(0, len(current_arr),7 * k):
        if current_arr[my_index:my_index+(7*k)] in patturn:
           pass
        else:
            return False
    return True

def ispassword(arr, k):
    patturn = [
        '000' * k + '11' * k + '0' * k + '1' * k,  # 0
        '00' * k + '11' * k + '00' * k + '1' * k,  # 1
        '00' * k + '1' * k + '00' * k + '11' * k,  # 2
        '0' * k + '1111' * k + '0' * k + '1' * k,  # 3
        '0' * k + '1' * k + '000' * k + '11' * k,  # 4
        '0' * k + '11' * k + '000' * k + '1' * k,  # 5
        '0' * k + '1' * k + '0' * k + '1111' * k,  # 6
        '0' * k + '111' * k + '0' * k + '11' * k,  # 7
        '0' * k + '11' * k + '0' * k + '111' * k,  # 8
        '000' * k + '1' * k + '0' * k + '11' * k,  # 9
    ]
    my_digit = []
    for my_index in range(0, len(arr),7 * k):
        my_digit.append(patturn.index(arr[my_index:my_index+(7*k)]) )
    istentimes = (my_digit[0] + my_digit[2] + my_digit[4] + my_digit[6]) * 3 + my_digit[1] + my_digit[3] + my_digit[5] + my_digit[7]
    # print(istentimes)
    if istentimes % 10 == 0:
        return sum(my_digit)
    else:
        return 0

#
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = 0
    already_have = []
    for n in range(N):
        arr = input()
        arr = arr.replace('0', '0000')
        arr = arr.replace('1', '0001')
        arr = arr.replace('2', '0010')
        arr = arr.replace('3', '0011')
        arr = arr.replace('4', '0100')
        arr = arr.replace('5', '0101')
        arr = arr.replace('6', '0110')
        arr = arr.replace('7', '0111')
        arr = arr.replace('8', '1000')
        arr = arr.replace('9', '1001')
        arr = arr.replace('A', '1010')
        arr = arr.replace('B', '1011')
        arr = arr.replace('C', '1100')
        arr = arr.replace('D', '1101')
        arr = arr.replace('E', '1110')
        arr = arr.replace('F', '1111')
        # print(arr)
        last_index = len(arr) - 1  # 배열의 끝점
        while True:
            if last_index <= 0:
                break
            if arr[last_index] == '1':
                k = 1
                while True:
                    start_index = last_index - (56 * k)
                    if start_index < 0:

                        last_index = start_index + (56*(k -1))
                        k = 1
                        break
                    # print(start_index+1)
                    # print(arr[start_index+1:last_index+1])
                    # print(len(arr[start_index+1:last_index+1]))
                    if isrightarr(arr[start_index+1:last_index+1], k) and arr[start_index+1:last_index+1] not in already_have:  # 내가 선택한 배열이 패스워드냐 아니냐
                        already_have.append(arr[start_index+1:last_index+1])
                        result += ispassword(arr[start_index+1:last_index+1], k)
                        last_index -= 56 * k - 1
                        k = 1
                            # print(last_index, 't')
                    else:
                        k += 1
                        # 만약 패스워드면 결과갚에 반영하고, last_index를 내가 선택한 배열의 마지막에서 시작하고 브레이크
                        # 패스워드가 아니면 포문으로 넘어가
            last_index -= 1
    print('#%s %s' % (tc, result))