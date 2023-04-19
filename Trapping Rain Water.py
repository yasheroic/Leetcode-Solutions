class Solution:
    def trap(self, height):
        """
        Compute the amount of water that can be trapped in the elevation map.

        Args:
            height (List[int]): The integer array representing the elevation map.

        Returns:
            int: The amount of water that can be trapped.
        """
        n = len(height)
        if n < 3:
            return 0

        left = 0
        right = n - 1
        left_max = right_max = trapped_water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    trapped_water += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    trapped_water += right_max - height[right]
                right -= 1

        return trapped_water
