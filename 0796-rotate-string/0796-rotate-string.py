class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            a=s[i:]+s[:i]
            if a==goal:
                return True
        return False