class Solution:
    def firstMissingPositive(self, nums):
        target = 1
        target = target << (2*31)
        print(target)
        return 2 **31

if __name__ == "__main__":
    nums = [1, 2, 0]
    solution = Solution()
    print(solution.firstMissingPositive(nums))