class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        i = 0
        j = 0
        while i < len(nums1):
            if nums1[i] != nums2[j]:
                j += 1
            else: # if they are equal
                temp = nums2[j:]
                print(temp)
                nextGreaterElement = -1
                for n in temp:
                    if nums2[j] < n:
                        nextGreaterElement = n
                        break
                ans.append(nextGreaterElement)
                j = 0
                i += 1
                

        return ans