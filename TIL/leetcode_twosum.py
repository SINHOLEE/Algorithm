'''
hash를 이용한 탐색
'''

# class Solution:
#
#     def twoSum(self, nums, target):
#         for i in range(len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     res = [i, j]
#                     break
#
#         return res
#
#
# class Solution:
#
#
#     def twoSum(self, nums, target):
#         dic = {}
#         for i in range(len(nums)):
#             temp = target - nums[i]
#             if dic.get(temp) == None:
#                 dic[nums[i]] = i
#             else:
#
#                 return [dic[temp], i]


class Solution:


    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i

        for i in range(len(nums)):
            temp = target - nums[i]
            if dic.get(temp) != None and dic.get(temp) != i:

                return [i, dic[temp]]

objec = Solution()
print(objec.twoSum([4,5,3,4,6,7,8,2,3,41,1,4,6,3,1], 4))