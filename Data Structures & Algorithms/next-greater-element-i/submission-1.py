class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Index = {}
        for index, num in enumerate(nums1):
            nums1Index[num] = index
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1Index[val]
                res[idx] = cur
            if cur in nums1Index:
                stack.append(cur)

        return res