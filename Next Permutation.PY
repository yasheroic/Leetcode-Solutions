class Solution:
    def nextPermutation(self, nums):
        # Step 1: Find the first decreasing element from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: If a decreasing element is found
        if i >= 0:
            # Step 3: Find the smallest element greater than nums[i]
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1

            # Step 4: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Step 5: Reverse the subarray from nums[i+1:]
        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums
