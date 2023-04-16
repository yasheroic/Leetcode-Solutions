class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # create a dictionary to keep track of the frequency of each letter in the ransom note
        freq = {}
        for c in ransomNote:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        # iterate through the magazine and subtract the frequency of each letter from the dictionary
        for c in magazine:
            if c in freq:
                freq[c] -= 1

        # if any of the frequencies is greater than 0, it means that the ransom note cannot be constructed
        for f in freq.values():
            if f > 0:
                return False

        # if we reach this point, it means that the ransom note can be constructed
        return True
