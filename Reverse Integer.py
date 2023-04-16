class Solution:
    def reverse(self, x: int) -> int:
        # Convert the integer to a string and check if it's negative
        is_negative = x < 0
        x_str = str(abs(x))
        
        # Reverse the string
        x_reverse_str = x_str[::-1]
        
        # Convert the reversed string back to an integer
        x_reverse = int(x_reverse_str)
        
        # Add back the negative sign if necessary and check if the result is within the 32-bit integer range
        if is_negative:
            x_reverse *= -1
        if x_reverse < -2**31 or x_reverse > 2**31 - 1:
            return 0
        return x_reverse
