class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for c in s:
            if c.isalnum():
                newS += c.lower()
        i = 0
        j = len(newS) - 1
        while i < j:
            if newS[i] != newS[j]:
                return False
            i += 1
            j -= 1
        return True