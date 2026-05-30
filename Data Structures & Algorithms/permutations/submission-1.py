class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums,0)
        return self.res

    def backtrack(self, nums: List[int], idx: int):
        if idx == len(nums):
            self.res.append(nums[:])
            return
        for i in range(idx, len(nums)):
            temp = nums[idx]
            nums[idx] = nums[i]
            nums[i] = temp
            self.backtrack(nums, idx + 1)
            temp = nums[idx]
            nums[idx] = nums[i]
            nums[i] = temp