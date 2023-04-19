class Solution:
    def combinationSum(self, candidates, target):
        """
        Return a list of all unique combinations of candidates where the chosen numbers sum to target.

        Args:
            candidates (List[int]): The array of distinct integers candidates.
            target (int): The target integer to sum up to.

        Returns:
            List[List[int]]: A list of all unique combinations of candidates that sum up to target.
        """
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            elif target < 0:
                return
            else:
                for i in range(start, len(candidates)):
                    backtrack(i, target - candidates[i], path + [candidates[i]])

        result = []
        candidates.sort()
        backtrack(0, target, [])
        return result
