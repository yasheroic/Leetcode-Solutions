class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if not haystack:
            return -1

        if len(needle) > len(haystack):
            return -1

        # Iterate through the haystack string
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring starting at index i in haystack is equal to needle
            if haystack[i:i+len(needle)] == needle:
                return i

        # If needle is not found in haystack, return -1
        return -1
