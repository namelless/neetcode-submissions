class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        return all([(count/len(words)).is_integer() for count in Counter(''.join(words)).values()])