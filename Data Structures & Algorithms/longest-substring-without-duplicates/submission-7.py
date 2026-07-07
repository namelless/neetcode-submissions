class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = defaultdict(set)
        max_len = int(bool(len(s)))
        for i, char in enumerate(s):
            for j in range(i+1):
                if char not in table[j]:
                    table[j].add(char)
                    max_len = max(max_len, len(table[j]))
                else:del table[j]
        return max_len
        