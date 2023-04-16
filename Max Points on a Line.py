from collections import defaultdict

class Solution:
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n

        max_count = 0
        for i in range(n):
            slope_count = defaultdict(int)
            for j in range(i+1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if dx == 0:
                    slope = float('inf')
                else:
                    slope = dy / dx
                slope_count[slope] += 1

            if slope_count:
                count = max(slope_count.values()) + 1
            else:
                count = 1

            max_count = max(max_count, count)

        return max_count
