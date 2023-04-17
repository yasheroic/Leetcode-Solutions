class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Define mapping of digits to letters
        mappings = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # Define recursive function to generate letter combinations
        def generate_combinations(digits, current_combination):
            if not digits:
                # Base case: no more digits to process, add current combination to result
                result.append(current_combination)
            else:
                # Recursive case: process next digit and add all possible letter combinations
                for letter in mappings[digits[0]]:
                    generate_combinations(digits[1:], current_combination + letter)

        # Initialize result list and call recursive function to generate letter combinations
        result = []
        generate_combinations(digits, '')

        return result
