class Solution:
    def nextPermutation(self, nums):
        target = -1
        length =len(nums)
        for i in range(length-2, -1, -1):
            if nums[i] < nums[i+1]:
                target = i
                break
        if target >= 0:
            for i in range(length-2, -1, -1):
                if nums[target] < nums[i+1]:
                    nums[target], nums[i+1] = nums[i+1], nums[target]

                    break
        idx = length -1
        target += 1

        while target < idx:
            nums[target], nums[idx] = nums[idx], nums[target]
            idx -= 1
            target += 1



ob = Solution()

print(ob.nextPermutation([3,2,1]))