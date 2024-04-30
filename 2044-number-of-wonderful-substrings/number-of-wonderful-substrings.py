from collections import defaultdict

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        total = 0
        n = len(word)
        count = defaultdict(int)
        count[0] = 1
        bitmask = 0
        
        for i in range(n):
            bitmask ^= 1 << (ord(word[i]) - ord('a'))
            total += count[bitmask]
            for j in range(10):
                total += count[bitmask ^ (1 << j)]
            count[bitmask] += 1
        
        return total