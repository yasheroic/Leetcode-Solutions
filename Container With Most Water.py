class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the area with the current left and right pointers
            area = min(height[left], height[right]) * (right - left)

            # Update the maximum area if the current area is greater
            max_area = max(max_area, area)

            # Move the pointer with the smaller height towards the middle
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
