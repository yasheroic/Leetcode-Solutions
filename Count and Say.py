class Solution:
    def countAndSay(self, n):
        """
        Return the nth term of the count-and-say sequence.

        Args:
            n (int): The positive integer representing the term in the sequence to return.

        Returns:
            str: The nth term of the count-and-say sequence.
        """
        if n == 1:
            return "1"

        prev = "1"
        for i in range(2, n+1):
            current = ""
            count = 1
            j = 1
            while j < len(prev):
                if prev[j] == prev[j-1]:
                    count += 1
                else:
                    current += str(count) + prev[j-1]
                    count = 1
                j += 1
            current += str(count) + prev[j-1]
            prev = current

        return prev
