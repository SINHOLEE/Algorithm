# from pprint import pprint
#
# # 사용자 지정 dfs
# nums = [ 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
#
# mat = [[0] * (max(nums) + 1) for _ in range(max(nums) + 1)]
#
# for i in range(0, len(nums), 2):
#     mat[nums[i]][nums[i+1]] = 1
#     mat[nums[i+1]][nums[i]] = 1
#
#
# visited = [False] * (max(nums) + 1)
#
# def zero_count(lists):
#     count = 0
#     for i in lists:
#         if i == 0:
#             count += 1
#     return count
#
# # stack 생성
# s = [0] * 100
#
# top = -1
# start = nums[0] # (1, 2)에서 1부터 시작
#
# #  push(nums[0])
# top += 1
# s[top] = nums[0]
#
# string = ''
# while len(s) != zero_count(s):
#     v = s[top]
#     # pop()
#     s[top] = 0
#
#     top -= 1
#
#     # 자기처리
#     if visited[v] == False:
#         visited[v] = True
#     # 만약 내가 지니고 있는 v가 True라면 다음 진도로 나가
#     else:
#         continue
#     # 출력을 위한 처리
#     vv = str(v)
#     string += vv
#
#
#     for j in range(len(mat[v])):
#         if mat[v][j] == 1 and visited[j] == False:
#
#             # push
#             top += 1
#             s[top] = j
#
# print(string)


# 재귀호출 dfs
nums = [ 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

mat = [[0] * (max(nums) + 1) for _ in range(max(nums) + 1)]

for i in range(0, len(nums), 2):
    mat[nums[i]][nums[i+1]] = 1
    mat[nums[i+1]][nums[i]] = 1


visited = [False] * (max(nums) + 1)
def DFS(v):
    global ssss

    if visited[v] == False:
        visited[v] = True
        ssss += str(v)

        for j in range(len(mat[v])):
            if visited[j] == False and mat[v][j] == 1:
                DFS(j)
    return ssss
ssss = ''

print(DFS(nums[0]))


