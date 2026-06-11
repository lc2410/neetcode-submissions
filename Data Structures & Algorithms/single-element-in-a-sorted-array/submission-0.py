class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 2  # Keep high bounded to safely check mid + 1

        while low <= high:
            mid = (low + high) // 2
            
            # If mid is odd, step back by 1 to make it even
            if mid % 2 == 1:
                mid -= 1
                
            # Check if the pair aligns correctly
            if nums[mid] == nums[mid + 1]:
                # Left side is paired properly; look to the right
                low = mid + 2
            else:
                # Left side has an unaligned element; look to the left
                high = mid - 1
                
        return nums[low]