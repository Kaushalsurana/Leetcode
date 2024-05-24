class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        if len(words) == 0:
            return 0
        if len(letters) == 0:
            return 0
        newletters = letters[:]
        curr_score = 0
        for i in words[0]:
            if i in newletters:
                newletters.remove(i)
                curr_score += score[ord(i)-ord('a')]
            else:
                return self.maxScoreWords(words[1:],letters,score)
        return max(curr_score+self.maxScoreWords(words[1:],newletters,score),self.maxScoreWords(words[1:],letters,score))