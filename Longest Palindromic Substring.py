class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        # Initialize a table of size n x n to store if a substring is palindrome or not
        # dp[i][j] = True if s[i:j+1] is palindrome, False otherwise
        dp = [[False] * n for _ in range(n)]
        
        # All substrings of length 1 are palindrome
        for i in range(n):
            dp[i][i] = True
        
        # All substrings of length 2 are palindrome if they are the same character
        max_len = 1
        start = 0
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                max_len = 2
                start = i
        
        # For substrings of length greater than 2, check if the first and last characters match
        # and if the substring between them is a palindrome
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i+k-1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if k > max_len:
                        max_len = k
                        start = i
        
        return s[start:start+max_len]
