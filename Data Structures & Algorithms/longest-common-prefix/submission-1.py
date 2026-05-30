class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])): # loop through the letters of the first string
            for s in strs: # loop through then the strs array
            # check the length are the same or the letter or the current letter of the inner string != the current of the first string
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]