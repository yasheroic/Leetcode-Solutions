class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams together in a list of strings.

        Args:
            strs (List[str]): The input list of strings.

        Returns:
            List[List[str]]: The grouped anagrams.
        """
        anagrams = {}
        for s in strs:
            # Sort the string to obtain the key
            key = ''.join(sorted(s))
            # Append the original string to the value list associated with the key
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
        # Convert the values of the hashmap into a list to obtain the grouped anagrams
        return list(anagrams.values())
