import itertools
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ["green_turban", "pants"]]


# 노가다
# def solution(clothes):
#     answer = 0
#     dic = {}
#
#     for c in clothes:
#         if c[1] in dic.keys():
#             dic[c[1]] += 1
#         else:
#             dic[c[1]] = 1
#     # print(dic)
#     keys = list(dic.keys())
#     # print(keys)
#     for i in range(1, (1<<len(list(dic)))):
#         temp = 1
#         for j in range(len(dic)):
#             if i & 1<<(len(dic) -1 -j):
#                 temp *= dic[keys[j]]
#         answer += temp
#     return answer

#수학
# def solution(clothes):
#     answer = 1
#     dic = {}
#
#     for c in clothes:
#         if c[1] in dic.keys():
#             dic[c[1]] += 1
#         else:
#             dic[c[1]] = 1
#
#     for key, value in dic.items():
#         answer *= (value + 1)
#     answer -= 1
#     return answer
# print(solution(clothes))

import collections

def solution(clothes):
    dic=collections.Counter()

    ans =1
    for i in clothes:
        dic[i[1]] += collections.Counter(i)[i[1]]
    for i in dic.keys():
        ans = ans*(dic[i]+1)
    ans = ans -1
    return ans
print(solution(clothes))
