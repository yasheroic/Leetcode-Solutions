class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array to use two-pointer approach
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            # If current element is same as previous element, skip it to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # Set two pointers to find pairs that sum up to -nums[i]
            j, k = i+1, len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    # Skip elements with same values to avoid duplicate triplets
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return res
