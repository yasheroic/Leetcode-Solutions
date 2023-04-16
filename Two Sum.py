class Solution:
    def twoSum(self, nums, target):
        # Loop through the array
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Check if the sum of the current pair is equal to the target
                if nums[i] + nums[j] == target:
                    return [i, j]
        # Return an empty list if no pair is found
        return []
