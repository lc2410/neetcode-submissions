class Solution:

    def fillDict(self, string: str, dictionary: dict):
        for c in string:
            if c not in dictionary:
                dictionary[c] = 0
            dictionary[c] += 1

    def isAnagram(self, s: str, t: str) -> bool:
        sCharDict = {}
        tCharDict = {}
        self.fillDict(s, sCharDict)
        self.fillDict(t, tCharDict)
        return sCharDict == tCharDict
        
        
