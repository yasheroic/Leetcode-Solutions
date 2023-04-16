class Solution:
    def lengthOfLongestSubstring(self, s):
        # Initialize the start and end indices of the sliding window
        start = 0
        end = 0

        # Initialize the set to store the characters in the current window
        window = set()

        # Initialize the maximum length
        max_length = 0

        # Loop until the end of the string is reached
        while end < len(s):
            # Check if the current character is not in the window
            if s[end] not in window:
                # Add the character to the window
                window.add(s[end])
                # Increase the end index
                end += 1
                # Update the maximum length if necessary
                max_length = max(max_length, end - start)
            else:
                # Remove the character at the start of the window
                window.remove(s[start])
                # Increase the start index
                start += 1

        return max_length
