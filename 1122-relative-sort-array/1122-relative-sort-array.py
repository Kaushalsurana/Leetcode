class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        b=[]
        for i in arr2:
            while i in arr1:
                b.append(i)
                arr1.remove(i)
        k=b+sorted(arr1)
        return k 