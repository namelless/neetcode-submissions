class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        chars = Counter(''.join(words))
        return all([(count/len(words)).is_integer() for count in chars.values()])