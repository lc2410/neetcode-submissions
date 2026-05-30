class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr)

        while len(arr[left:right]) > k:
            if abs(arr[left] - x) < abs(arr[right-1] - x) or abs(arr[left] - x) == abs(arr[right-1] - x):
                right -= 1
            else:
                left += 1

        return arr[left:right]