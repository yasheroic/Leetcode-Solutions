class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize left and right pointers
        left, right = 0, len(nums) - 1

        # Binary search algorithm to find the index where target would be inserted
        while left <= right:
            mid = (left + right) // 2  # Calculate the middle index

            # If the middle element is equal to the target, return the index
            if nums[mid] == target:
                return mid
            # If the middle element is less than the target, continue search on the right side
            elif nums[mid] < target:
                left = mid + 1
            # If the middle element is greater than the target, continue search on the left side
            else:
                right = mid - 1

        # If target is not found, return the index where it would be inserted
        return left
