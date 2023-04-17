class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        for word in strs[1:]:
            while word[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

def _driver():
    test_cases = [
        ["flower","flow","flight"],
        ["dog","racecar","car"],
        ["hello","hell","hello world"],
        ["","test","testing"],
        ["abc","abcde","abcdefg"],
    ]
    for i, test_case in enumerate(test_cases):
        print(f"Example {i+1}: {Solution().longestCommonPrefix(test_case)}")

if __name__ == "__main__":
    _driver()
