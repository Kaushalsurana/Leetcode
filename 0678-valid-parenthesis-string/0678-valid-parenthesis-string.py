class Solution:
    def checkValidString(self, s: str) -> bool:
        count1=0
        count2=0
        for i in range(len(s)):
            if s[i]=='(':
                count1+=1
            elif s[i]==')':
                count1-=1
            elif s[i]=='*':
                count2+=1
            if count1<0:
                count2-=1
                count1+=1
                if count2<0:
                    return False
        count1=0
        count2=0
        for i in reversed(range(len(s))):
            if s[i]==')':
                count1+=1
            elif s[i]=='(':
                count1-=1
            elif s[i]=='*':
                count2+=1
            if count1<0:
                count2-=1
                count1+=1
                if count2<0:
                    return False
        return True
        