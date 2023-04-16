class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers can never be a palindrome
        if x < 0:
            return False
        
        # Reverse the number using math
        reverse = 0
        original = x
        while x > 0:
            reverse = reverse * 10 + x % 10
            x //= 10
        
        # Check if the reversed number is the same as the original
        return reverse == original
