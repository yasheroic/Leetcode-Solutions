class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible unique permutations of an array containing duplicates.

        Args:
            nums (List[int]): The input array.

        Returns:
            List[List[int]]: A list of all possible unique permutations of the input array.
        """
        def backtrack(first):
            # Base case: if all elements have been used, append current permutation to results
            if first == n:
                results.append(nums[:])
            used = set()
            for i in range(first, n):
                # Skip elements that have been used in this position before
                if nums[i] in used:
                    continue
                # Swap elements to create a new permutation
                nums[first], nums[i] = nums[i], nums[first]
                # Recursively generate permutations with the next element as the first
                backtrack(first + 1)
                # Undo the swap to restore the original array
                nums[first], nums[i] = nums[i], nums[first]
                # Add current element to used set to avoid duplicates in the same position
                used.add(nums[i])

        n = len(nums)
        results = []
        backtrack(0)
        return results
