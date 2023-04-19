class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Find the minimum number of jumps to reach the last index in an array.

        Args:
            nums (List[int]): The input array.

        Returns:
            int: The minimum number of jumps to reach the last index.
        """
        n = len(nums)
        # Initialize variables to keep track of current and farthest reachable index
        current_jump = 0
        farthest_jump = 0
        # Initialize variable to keep track of minimum number of jumps
        jumps = 0

        for i in range(n - 1):
            # Update the farthest reachable index from current position
            farthest_jump = max(farthest_jump, i + nums[i])
            # If current position is equal to current jump, update current jump to farthest jump
            if i == current_jump:
                current_jump = farthest_jump
                jumps += 1

        return jumps
