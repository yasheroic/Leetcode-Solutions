class Solution:
    def firstMissingPositive(self, nums):
        """
        Return the smallest missing positive integer in the array.

        Args:
            nums (List[int]): The unsorted integer array.

        Returns:
            int: The smallest missing positive integer.
        """
        n = len(nums)

        # Step 1: Mark all negative numbers and numbers larger than n as n+1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # Step 2: Mark numbers as negative based on their indices
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        # Step 3: Find the first missing positive integer
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        # If all numbers are negative, the first missing positive integer is n + 1
        return n + 1
