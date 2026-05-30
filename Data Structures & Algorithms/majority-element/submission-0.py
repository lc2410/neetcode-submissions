class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        interations = 1
        for i in range(1, len(nums)):
            if nums[i] == ans:
                interations += 1
            else:
                interations -= 1
            
            if interations < 0:
                ans = nums[i]
                interations = 1
        return ans