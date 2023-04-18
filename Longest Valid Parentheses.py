class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Initialize a stack to keep track of indices of opening parentheses
        stack = [-1]
        # Initialize a variable to store the length of the longest valid parentheses substring
        max_len = 0

        # Iterate through the string from left to right
        for i in range(len(s)):
            if s[i] == '(':
                # Push the index of the opening parenthesis to the stack
                stack.append(i)
            else:
                # Pop the top element from the stack if it's not empty
                if len(stack) > 1:
                    stack.pop()
                    # Update the maximum length with the length of the current valid parentheses substring
                    max_len = max(max_len, i - stack[-1])
                else:
                    # If the stack is empty, push the current index as a marker for the next valid substring
                    stack[0] = i

        return max_len
