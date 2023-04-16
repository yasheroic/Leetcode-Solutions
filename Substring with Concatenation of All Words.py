from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_count = Counter(words)
        word_len = len(words[0])
        total_len = len(words) * word_len

        result = []
        for i in range(len(s) - total_len + 1):
            current_count = Counter()
            for j in range(i, i + total_len, word_len):
                word = s[j:j+word_len]
                if word not in word_count:
                    break
                current_count[word] += 1
                if current_count[word] > word_count[word]:
                    break
            else:
                result.append(i)

        return result
