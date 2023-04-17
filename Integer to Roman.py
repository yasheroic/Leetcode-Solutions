class Solution:
    def intToRoman(self, num: int) -> str:
        # Define two lists to represent the Roman numerals and their corresponding values
        roman_numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        roman_numeral = ""
        i = 0

        # Loop through the values list and keep adding the corresponding Roman numerals to the result string
        while num > 0:
            # If the current value is less than or equal to the number, subtract it from the number and add the corresponding Roman numeral to the result string
            if values[i] <= num:
                roman_numeral += roman_numerals[i]
                num -= values[i]
            else:
                i += 1

        return roman_numeral
