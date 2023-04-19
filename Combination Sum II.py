class Solution:
    def combinationSum2(self, candidates, target):
        """
        Return a list of all unique combinations of candidates where the chosen numbers sum to target.

        Args:
            candidates (List[int]): The collection of candidate numbers.
            target (int): The target number to sum up to.

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
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        result = []
        candidates.sort()
        backtrack(0, target, [])
        return result
