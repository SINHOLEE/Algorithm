
class Solution:

    def find_duplicate(self, nums):
        a_idx = nums[0]
        b_idx = nums[0]

        while True:
            a_idx = nums[a_idx]
            b_idx = nums[nums[b_idx]]

            # print(a_idx, b_idx)
            if a_idx == b_idx:
                break
        a = nums[0]
        b = a_idx
        while a != b:
            # print(a, b)
            a = nums[a]
            b = nums[b]

        return a


solution = Solution()
print(solution.find_duplicate([1, 2, 3, 4, 4]))
