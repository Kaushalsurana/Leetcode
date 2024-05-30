class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        a=0
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                b=0
                for k in range(i,j):
                    b^=arr[k]
                c=0
                for l in range(j,n):
                    c^=arr[l]
                    if b==c:
                        a+=1
        return a
                