class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=strs[0]
        for i in range(1,len(strs)):
            p=''
            for j in range(min(len(a),len(strs[i]))):
                if a[j]!=strs[i][j]:
                    break
                p+=a[j]
            a=p
        return a


