class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n=len(names)
        k = list(zip(heights, names))
        k.sort(reverse=True, key=lambda x: x[0])
        for i in range(n):
            names[i]=k[i][1]
        return names