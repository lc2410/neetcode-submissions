class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] == "[" or s[i] == "(" or s[i] == "{":
                stack.append(s[i])
            else:
                val = ""
                if len(stack) != 0:
                    val = stack.pop()
                par = val + s[i]
                if par != "[]" and par != "{}" and par != "()":
                    return False
        return len(stack) == 0