class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=defaultdict(list)
        for i in strs:
            c=[0]*26
            for j in i:
                c[ord(j)-ord("a")]+=1
            a[tuple(c)].append(i)
        return list(a.values())