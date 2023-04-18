class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Initialize the left and right pointers
        left, right = 0, len(nums) - 1
        result = [-1, -1]

        # Binary search algorithm to find the left boundary
        while left <= right:
            mid = (left + right) // 2  # Calculate the middle index

            # Check if the middle element is the target
            if nums[mid] == target:
                result[0] = mid
                right = mid - 1  # Continue search on the left side
            # If the middle element is less than the target
            elif nums[mid] < target:
                left = mid + 1
            # If the middle element is greater than the target
            else:
                right = mid - 1

        # Binary search algorithm to find the right boundary
        left, right = 0, len(nums) - 1  # Reset the pointers
        while left <= right:
            mid = (left + right) // 2  # Calculate the middle index

            # Check if the middle element is the target
            if nums[mid] == target:
                result[1] = mid
                left = mid + 1  # Continue search on the right side
            # If the middle element is less than the target
            elif nums[mid] < target:
                left = mid + 1
            # If the middle element is greater than the target
            else:
                right = mid - 1

        return result
