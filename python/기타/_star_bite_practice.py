

# 부분집합 비트로 보기

# bit = [0, 0, 0, 0]
# n = 0
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
                
#                 print(bit, n )
#                 n += 1


li = [1, 2, 3, 4]
part_of_set = []
for i in range(1<<len(li)):
    
    temp = []
    for j in range(len(li)):
        if i &(1<<j):
            temp += [li[j]]
    part_of_set += [temp]
    
print(part_of_set)

# 조합.... 4Ci의 경우를 만들 수 있다!~
for index in range(len(part_of_set)):
    for i in range(len(li)+1):
        if i == len(part_of_set[index]):
            print(i, part_of_set[index])