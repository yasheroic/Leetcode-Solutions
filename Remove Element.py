class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        # Initialize pointers
        slow = 0
        fast = 0

        # Iterate through the array
        while fast < len(nums):
            # If the current element is not equal to the value to be removed,
            # move the slow pointer and update the array
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        # Return the number of elements in nums which are not equal to val (slow)
        return slow
