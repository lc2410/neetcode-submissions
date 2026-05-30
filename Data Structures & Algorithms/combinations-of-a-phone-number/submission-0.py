class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numPad = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz", 0: "*"}
        ans = []
        
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                ans.append(curStr)
                return
            for c in numPad[int(digits[i])]:
                backtrack(i+1, curStr+c)

        if digits:
            backtrack(0,"")

        return ans