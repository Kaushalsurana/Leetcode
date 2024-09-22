class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        n=0
        banned=set(bannedWords)
        for i in message:
            if i in banned:
                n+=1
        if n>=2:
            return True
        else:
            return False