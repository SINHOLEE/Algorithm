class Solution:
    def jump(self, nums):
        goal = len(nums) - 1

        dp = [0] + [0]* (goal)
        flag = False
        for i in range(goal):
            temp = i+1

            for j in range(nums[i]):
                if temp > goal:
                    break
                if dp[temp] == 0:
                    dp[temp] = dp[i]+1
                else:
                    if dp[temp] > dp[i] + 1:
                        dp[temp] = dp[i] + 1
                temp += 1

        return dp[goal]

ob = Solution()

print(ob.jump([5]))

## 답코드..
## 하지만 이해가 가지 않아.
class Solution:
    def jump(self, nums):
        if len(nums) == 1:
            return 0

        steps = nums[0]
        maxReach = nums[0]
        jumps = 0

        for i in range(1, len(nums) - 1):
            maxReach = max(maxReach, nums[i] + i)
            steps -= 1
            if steps == 0:
                steps = maxReach - i
                jumps += 1

        return jumps + 1