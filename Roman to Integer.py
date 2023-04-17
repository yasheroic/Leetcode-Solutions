class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dictionary to store the values of Roman numerals
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # Initialize the result variable and the previous value variable
        result = 0
        prev_value = 0

        # Iterate through each character in the string in reverse order
        for char in s[::-1]:
            # Get the value of the current character from the dictionary
            curr_value = roman_values[char]

            # If the current value is less than the previous value, subtract it from the result
            if curr_value < prev_value:
                result -= curr_value
            # Otherwise, add it to the result
            else:
                result += curr_value

            # Update the previous value
            prev_value = curr_value

        return result
