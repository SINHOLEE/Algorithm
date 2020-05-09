

def solution(expression):
    orders = [('-', '*', '+'),
              ('-', '+', '*'),
              ('*', '-', '+'),
              ('*',  '+', '-'),
              ('+', '-', '*'),
              ('+', '*', '-')

           ]


    def op(a, b, o):
        if o == '*':
            return a * b
        elif o == '-':
            return a - b
        else:
            return a + b


    answer = 0
    nums = list(map(int, expression.replace('-',' ').replace('*', ' ').replace('+', ' ').split()))
    operations = list(expression.replace('0','').replace('1','').replace('2','').replace('3','').\
        replace('4','').replace('5','').replace('6','').\
        replace('7','').replace('8','').replace('9',''))
    new_list = []
    while True:
        if len(operations) == 0 and len(nums) == 0:
            break
        if len(nums):
            new_list.append(nums.pop(0))
        if len(operations):
            new_list.append(operations.pop(0))

    for ord in orders:
        temp = 0
        temp_list = new_list[:] # copy
        for opr in ord:
            i = 1
            le = len(temp_list)
            while True:
                if len(temp_list) == 1:
                   break
                if le <= i:
                    break
                if temp_list[i] == opr:
                    temp_list = temp_list[:i-1] + [op(temp_list[i-1], temp_list[i+1], temp_list[i])] + temp_list[i+2:]
                    le -= 2
                else:
                    i += 2
        answer = max(abs(temp_list[0]), answer)

    return answer


solution("100-200*300-500+20")