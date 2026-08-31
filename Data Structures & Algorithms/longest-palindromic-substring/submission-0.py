class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        # dp[i][j] represents whether the substring s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]
        
        start_index = 0
        max_length = 1

        # Base case: every single character is a palindrome
        for i in range(n):
            dp[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                if s[i] == s[j]:
                    # Length 2 only needs matching endpoints. 
                    # Longer strings need the inner string to be a palindrome too.
                    if length == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        
                        # Save the boundaries of the longest palindrome found so far
                        if length > max_length:
                            start_index = i
                            max_length = length

        return s[start_index : start_index + max_length]
