class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sHashMap = {}
        for char in s:
            if char in sHashMap:
                sHashMap[char] += 1
            else:
                sHashMap[char] = 1
        for char in t:
            if char not in sHashMap:
                return False
            sHashMap[char] -= 1
            if sHashMap[char] == 0:
                sHashMap.pop(char)
        return True