class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible permutations of an array.

        Args:
            nums (List[int]): The input array.

        Returns:
            List[List[int]]: A list of all possible permutations of the input array.
        """
        def backtrack(first):
            # Base case: if all elements have been used, append current permutation to results
            if first == n:
                results.append(nums[:])
            for i in range(first, n):
                # Swap elements to create a new permutation
                nums[first], nums[i] = nums[i], nums[first]
                # Recursively generate permutations with the next element as the first
                backtrack(first + 1)
                # Undo the swap to restore the original array
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        results = []
        backtrack(0)
        return results
