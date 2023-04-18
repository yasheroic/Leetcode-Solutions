class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize pointers
        slow = 0
        fast = 1

        # Iterate through the array
        while fast < len(nums):
            # If the current element is different from the previous element,
            # move the slow pointer and update the array
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        # Return the number of unique elements (slow + 1)
        return slow + 1
