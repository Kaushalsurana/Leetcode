class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        b=[]
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                b.append([arr[i]/arr[j],arr[i],arr[j]])
        b.sort()
        return [b[k-1][1],b[k-1][2]]