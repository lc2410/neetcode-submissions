class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)
        s1 = ''.join(sorted(s1))
        while right <= len(s2):
            substringS2 = s2[left:right]
            sortedSubstringS2 = ''.join(sorted(substringS2))
            print(sortedSubstringS2)
            if s1 == sortedSubstringS2:
                return True
            left += 1
            right += 1
        return False