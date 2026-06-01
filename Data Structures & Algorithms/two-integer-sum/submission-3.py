class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        ans = [None] * 2
        for ind, num in enumerate(nums):
            hashmap[num] = ind
        for i in range(len(nums)-1, -1, -1):
            diff = target - nums[i]
            if diff in hashmap and i != hashmap[diff]:
                ans[0] = i
                ans[1] = hashmap[diff]
        return ans