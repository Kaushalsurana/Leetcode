class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n=26
        arr=[[float('inf') for j in range(n)]for i in range(n)]
        for i in range(n):
            arr[i][i]=0
        for i in range(len(original)):
            ans=min(arr[ord(original[i])-97][ord(changed[i])-97],cost[i])
            arr[ord(original[i])-97][ord(changed[i])-97]=ans
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if arr[i][j]>=arr[i][k]+arr[k][j]:
                        arr[i][j]=arr[i][k]+arr[k][j]
        ans=0
        for i in range(len(source)):
            if arr[ord(source[i])-97][ord(target[i])-97]==float('inf'):
                return -1
            ans+=arr[ord(source[i])-97][ord(target[i])-97]
        return ans