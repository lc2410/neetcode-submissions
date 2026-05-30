class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        currMin = nums[0]
        while left <= right:
            mid = left+(right-left) // 2
            currMin = min(currMin, nums[mid])
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1

        if nums[-1] < nums[0]:
            return currMin
        return nums[0]