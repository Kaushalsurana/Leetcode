class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        total_count = 0
        current_prefix = 0  
        frequency = [0] * 1024  
        frequency[0] = 1  

        for char in word:
            current_prefix ^= 1 << ord(char) - ord('a')
            total_count += frequency[current_prefix]
            total_count += sum(frequency[current_prefix ^ 1 << i] for i in range(10))
            frequency[current_prefix] += 1

        return total_count