class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        prev1 = nums[0]
        prev2 = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            maxMoney = max(prev1+nums[i], prev2)
            prev1 = prev2
            prev2 = maxMoney
        return prev2
