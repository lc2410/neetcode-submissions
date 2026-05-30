class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #0,1,2,3,4,5,6
        numSet = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest