class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize the left and right pointers
        left, right = 0, len(nums) - 1

        # Binary search algorithm
        while left <= right:
            mid = (left + right) // 2  # Calculate the middle index

            # Check if the middle element is the target
            if nums[mid] == target:
                return mid

            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
                # Check if the target is in the left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # If the left half is not sorted, the right half must be sorted
            else:
                # Check if the target is in the right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # If the target is not found, return -1
        return -1
