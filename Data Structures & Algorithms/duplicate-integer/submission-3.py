class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = set()
        for num in nums:
            uniqueNums.add(num)
        return len(uniqueNums) != len(nums)