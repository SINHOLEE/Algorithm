import sys
sys.setrecursionlimit(2000)
from decimal import Decimal

input_stream = input()
arr = []
s = ""
for i in range(len(input_stream)):
    if input_stream[i] not in ("+", "*", "-", "/"):
        s += input_stream[i]
        if i == len(input_stream)-1:
            arr.append(Decimal(s))
    else:
        if i == 0:
            s += input_stream[i]
            continue
        arr.append(Decimal(s))
        arr.append(input_stream[i])
        s = ""

# 우선순서 사전
operator_dic = {
    "*": 1,
    "/": 1,
    "+": 0,
    "-": 0
}


def operator(a, b, op):
    if op == "*":
        return a * b
    if op == "/":
        return a // b
    if op == "+":
        return a + b
    if op == "-":
        return a - b


def calc(lis, depth):
    if depth == 0:
        return lis[0]
    if operator_dic[lis[1]] == operator_dic[lis[-2]]:
        a, op, b = lis[0], lis[1], lis[2]
        temp1 = operator(a, b, op)
        aa, oopp, bb = lis[-3], lis[-2], lis[-1]
        temp2 = operator(aa, bb, oopp)
        if temp1 >= temp2:
            temp = [temp1] + lis[3:]
        else:
            temp = lis[:-3] + [temp2]
    elif operator_dic[lis[1]] > operator_dic[lis[-2]]:
        a, op, b = lis[0], lis[1], lis[2]
        temp = [operator(a, b, op)] + lis[3:]
    else:
        a, op, b = lis[-3], lis[-2], lis[-1]
        temp = lis[:-3] + [operator(a, b, op)]
    return calc(temp, depth-1)


print(calc(arr, len(arr) // 2))

