import time
start = time.time()
n = int(input())
arr = list(map(str, input()))


def cal(temp):
    if len(temp) == 1:
        return temp[0]
    elif len(temp) == 3:
        if temp[1] == '+':
            new = temp[0] + temp[2]

            return cal([new])
        elif temp[1] =='*':
            new = temp[0] * temp[2]
            return cal([new])
        else:
            new = temp[0] - temp[2]

            return cal([new])
    else:
        if temp[1] == '+':
            new = temp[0] + temp[2]
            return cal([new] + temp[3:] )
        elif temp[1] == '*':
            new = temp[0] * temp[2]
            return cal([new] + temp[3:] )
        else:
            new = temp[0] - temp[2]

            return cal([new] + temp[3:])

# print(cal([1, '*', 3, "*", 4, '-', 2]))

for i in range(len(arr)):
    if i % 2 == 0:
        arr[i] = int(arr[i])

# print(arr)
max_val = (-2) ** 33
for i in range(0, (1<< n//2) -1):
    value = 0
    temp = str(bin(i))[2:]
    length = len(temp)
    my_arr = list(map(int, temp))
    if length < n//2:
        my_arr = [0] * (n//2 - length) + my_arr
    print(my_arr)
#     check = False
#     for x in range(len(my_arr)-1):
#         if my_arr[x] == 1 and my_arr[x+1] == 1:
#             check = True
#             break
#     if check:
#         continue
#     bucket = []
#     temp = []
#     val = 0
#     for k in range(len(my_arr)):
#         if k == len(my_arr) - 1:  #끝에서.
#             if my_arr[k]:
#                 temp.append(arr[k * 2])
#                 temp.append(arr[(k * 2) + 1])
#                 temp.append(arr[(k * 2) + 2])
#                 new_digit = cal(temp)
#                 bucket.append(new_digit)
#             else:
#                 if temp:
#                     temp.append(arr[k * 2])
#                     new_digit = cal(temp)
#                     bucket.append(new_digit)
#                     bucket.append(arr[(k * 2) + 1])
#                     bucket.append(arr[(k * 2) + 2])
#                 else:
#                     bucket.append(arr[(k*2)])
#                     bucket.append(arr[(k*2)+1])
#                     bucket.append(arr[(k*2)+2])
#         else:  # 처음부터 끝 전까지
#             if my_arr[k]:
#                 temp.append(arr[k*2])
#                 temp.append(arr[(k*2)+1])
#             else:
#                 if temp:
#                     temp.append(arr[k*2])
#                     bucket.append(cal(temp))
#                     temp = []
#                 else:
#                     bucket.append(arr[k*2])
#                 bucket.append(arr[(k*2)+1])
#     val = cal(bucket)
#     if max_val < val:
#         max_val = val
#     # val = cal(temp)
#     # print(arr[item])
#     # print()
# if n == 1:
#     print(arr[0])
# else:
#     print(max_val)