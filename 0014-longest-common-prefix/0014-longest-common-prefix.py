class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p=strs[0]
        for i in range(1,len(strs)):
            new=""
            for j in range(min(len(p),len(strs[i]))):
                if p[j]==strs[i][j]:
                    new+=p[j]
                else:
                    break
            p=new
        return p

