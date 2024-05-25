class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict) 
        memo = {} 
        
        def dfs(start):
            if start in memo:
                return memo[start]
            
            if start == len(s):
                return [""] 
            results = []
            
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    remaining_sentences = dfs(end)
                    for sentence in remaining_sentences:
                        if sentence:
                            results.append(word + " " + sentence)
                        else:
                            results.append(word)
            
            memo[start] = results
            return results
        
        return dfs(0)