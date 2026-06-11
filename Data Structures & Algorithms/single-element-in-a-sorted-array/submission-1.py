class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if r == 0:
            return nums[0]
        while l <= r:
            if nums[l] != nums[l+1]:
                return nums[l]
            if nums[r] != nums[r-1]:
                return nums[r]

            r -= 2
            l += 2