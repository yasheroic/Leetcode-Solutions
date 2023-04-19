class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Check if an input string matches a wildcard pattern.

        Args:
            s (str): The input string to match.
            p (str): The wildcard pattern to match against.

        Returns:
            bool: True if the input string matches the wildcard pattern, False otherwise.
        """
        # Initialize pointers for the input string and pattern
        i, j = 0, 0
        # Initialize pointers to track the last '*' position and the corresponding character in s
        last_star = -1
        last_star_match = 0

        while i < len(s):
            if j < len(p) and (p[j] == '?' or s[i] == p[j]):
                # If current characters match or pattern has '?', move both pointers forward
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                # If pattern has '*', update last_star and last_star_match pointers
                last_star = j
                last_star_match = i
                j += 1
            elif last_star != -1:
                # If pattern does not match and last_star exists, backtrack to last_star_match
                j = last_star + 1
                last_star_match += 1
                i = last_star_match
            else:
                # If no match is found and there is no '*', return False
                return False

        # Check if there are any remaining characters in pattern after s ends
        while j < len(p) and p[j] == '*':
            j += 1

        # If pattern is exhausted, return True, else False
        return j == len(p)
