class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Multiply two non-negative integers represented as strings.

        Args:
            num1 (str): The first non-negative integer as a string.
            num2 (str): The second non-negative integer as a string.

        Returns:
            str: The product of num1 and num2 as a string.
        """
        if num1 == "0" or num2 == "0":
            return "0"

        len1, len2 = len(num1), len(num2)
        result = [0] * (len1 + len2)

        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                carry = product // 10
                sum = product % 10 + result[i + j + 1]
                result[i + j + 1] = sum % 10
                result[i + j] += sum // 10 + carry

        # Convert the result to a string
        return "".join(map(str, result)).lstrip("0") or "0"
